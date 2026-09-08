#!/usr/bin/env python3
"""Gera legenda .ass estilo nativo do Instagram: branco, negrito, sem fundo,
uma linha por bloco, ate 25 caracteres, com respiro lateral, 1a letra maiuscula."""
import argparse
import json


def seg_time(t):
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return f"{h:01d}:{m:02d}:{s:05.2f}"


def agrupar_em_blocos(palavras, max_chars=25):
    # Ajusta capitalizacao real: maiuscula so na 1a palavra do video e apos
    # pontuacao de fim de frase (. ! ?). Preserva o resto como o Whisper transcreveu
    # (nomes proprios ja vem certos, meio de frase fica minusculo).
    palavras = [dict(w, word=w["word"]) for w in palavras]
    nova_frase = True
    for w in palavras:
        word = w["word"].strip()
        if not word:
            continue
        if nova_frase:
            word = word[0].upper() + word[1:] if len(word) > 1 else word.upper()
        else:
            word = word[0].lower() + word[1:] if word[:1].isupper() and not word[1:2].isupper() else word
        w["word"] = " " + word if w["word"].startswith(" ") else word
        nova_frase = word.rstrip()[-1:] in ".!?" if word.rstrip() else nova_frase

    blocos = []
    atual = []
    ini_bloco = None
    texto_atual = ""
    for w in palavras:
        word = w["word"].strip()
        if ini_bloco is None:
            ini_bloco = w["start"]
        candidato = (texto_atual + " " + word).strip() if texto_atual else word
        if len(candidato) > max_chars and texto_atual:
            blocos.append((ini_bloco, prev_end, texto_atual))
            atual = [word]
            texto_atual = word
            ini_bloco = w["start"]
        else:
            texto_atual = candidato
            atual.append(word)
        prev_end = w["end"]
    if texto_atual:
        blocos.append((ini_bloco, prev_end, texto_atual))

    return blocos


def main():
    p = argparse.ArgumentParser()
    p.add_argument("palavras_json")
    p.add_argument("--out", required=True)
    p.add_argument("--largura", type=int, default=1080)
    p.add_argument("--altura", type=int, default=1920)
    p.add_argument("--fonte", default="Helvetica Neue")
    p.add_argument("--fontsize", type=int, default=58)
    p.add_argument("--marginv", type=int, default=620)
    p.add_argument("--marginlr", type=int, default=90)
    p.add_argument("--max-chars", type=int, default=25)
    args = p.parse_args()

    with open(args.palavras_json, encoding="utf-8") as f:
        palavras = json.load(f)

    blocos = agrupar_em_blocos(palavras, max_chars=args.max_chars)

    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {args.largura}
PlayResY: {args.altura}

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, Outline, Shadow, Alignment, MarginL, MarginR, MarginV
Style: Default,{args.fonte},{args.fontsize},&H00FFFFFF,&H00000000,&H00000000,1,2,1,2,{args.marginlr},{args.marginlr},{args.marginv}

[Events]
Format: Layer, Start, End, Style, Text
"""
    lines = [header]
    for b_ini, b_fim, texto in blocos:
        lines.append(f"Dialogue: 0,{seg_time(b_ini)},{seg_time(b_fim)},Default,{texto}\n")

    with open(args.out, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"Legenda gerada: {args.out} ({len(blocos)} blocos)")


if __name__ == "__main__":
    main()
