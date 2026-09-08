#!/usr/bin/env python3
"""
Corta um trecho do video original, reenquadra para 9:16 (ou outro aspect ratio) e queima
legenda estatica (.ass) usando a fonte informada. Tudo via ffmpeg local.

Uso:
  python3 cortar_legendar.py video.mp4 --inicio 723 --fim 761 \
      --palavras palavras.json --fonte "Montserrat" --out corte-01.mp4

  palavras.json: lista de {"start": float, "end": float, "word": str} relativos ao video ORIGINAL
  (a mesma escala de tempo da transcricao completa).
"""
import argparse
import json
import subprocess
import tempfile
import os


def seg_time(t):
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return f"{h:01d}:{m:02d}:{s:05.2f}"


def agrupar_em_blocos(palavras, inicio, fim, max_palavras=7, max_dur=3.0):
    blocos = []
    atual = []
    ini_bloco = None
    for w in palavras:
        if w["end"] < inicio or w["start"] > fim:
            continue
        if ini_bloco is None:
            ini_bloco = w["start"]
        atual.append(w["word"].strip())
        dur = w["end"] - ini_bloco
        if len(atual) >= max_palavras or dur >= max_dur:
            blocos.append((ini_bloco, w["end"], " ".join(atual)))
            atual = []
            ini_bloco = None
    if atual:
        blocos.append((ini_bloco, palavras[-1]["end"], " ".join(atual)))
    return blocos


def gerar_ass(blocos, inicio, fonte, path_ass, largura=1080, altura=1920):
    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {largura}
PlayResY: {altura}

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, Outline, Shadow, Alignment, MarginV
Style: Default,{fonte},64,&H00FFFFFF,&H00000000,&H80000000,1,3,0,2,180

[Events]
Format: Layer, Start, End, Style, Text
"""
    lines = [header]
    for b_ini, b_fim, texto in blocos:
        rel_ini = max(0, b_ini - inicio)
        rel_fim = max(rel_ini + 0.3, b_fim - inicio)
        lines.append(f"Dialogue: 0,{seg_time(rel_ini)},{seg_time(rel_fim)},Default,{texto}\n")
    with open(path_ass, "w", encoding="utf-8") as f:
        f.writelines(lines)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("video")
    p.add_argument("--inicio", type=float, required=True)
    p.add_argument("--fim", type=float, required=True)
    p.add_argument("--palavras", required=True, help="JSON com lista de palavras com timestamps do video original")
    p.add_argument("--fonte", required=True, help="Nome da fonte (ou nome registrado do arquivo .ttf/.otf)")
    p.add_argument("--fontsdir", default=None, help="Pasta com o arquivo .ttf/.otf, se for fonte custom")
    p.add_argument("--out", required=True)
    p.add_argument("--aspect", default="9:16", choices=["9:16", "16:9", "1:1"])
    args = p.parse_args()

    with open(args.palavras, encoding="utf-8") as f:
        palavras = json.load(f)

    blocos = agrupar_em_blocos(palavras, args.inicio, args.fim)

    crop_filters = {
        "9:16": "crop=ih*9/16:ih,scale=1080:1920",
        "16:9": "crop=iw:iw*9/16,scale=1920:1080",
        "1:1": "crop=ih:ih,scale=1080:1080",
    }
    crop = crop_filters[args.aspect]

    with tempfile.TemporaryDirectory() as tmp:
        recorte = os.path.join(tmp, "recorte.mp4")
        ass_path = os.path.join(tmp, "legenda.ass")

        largura, altura = (1080, 1920) if args.aspect == "9:16" else ((1920, 1080) if args.aspect == "16:9" else (1080, 1080))
        gerar_ass(blocos, args.inicio, args.fonte, ass_path, largura, altura)

        subprocess.run([
            "ffmpeg", "-y", "-ss", str(args.inicio), "-to", str(args.fim),
            "-i", args.video, "-c:v", "libx264", "-c:a", "aac", recorte,
        ], check=True)

        vf = crop
        if args.fontsdir:
            vf += f",ass={ass_path}:fontsdir={args.fontsdir}"
        else:
            vf += f",ass={ass_path}"

        subprocess.run([
            "ffmpeg", "-y", "-i", recorte, "-vf", vf,
            "-c:v", "libx264", "-crf", "18", "-preset", "medium",
            "-c:a", "aac", "-b:a", "192k", args.out,
        ], check=True)

    print(f"Corte final: {args.out}")


if __name__ == "__main__":
    main()
