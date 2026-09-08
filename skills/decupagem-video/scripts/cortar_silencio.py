#!/usr/bin/env python3
"""Detecta silencio via ffmpeg silencedetect, gera lista de segmentos "vivos"
(com pequena folga nas bordas) e um mapa de tempo original->novo para remapear
timestamps de palavras da transcricao."""
import argparse
import json
import re
import subprocess


def detectar_silencios(video, noise_db=-28, min_dur=0.35):
    cmd = [
        "ffmpeg", "-i", video, "-af",
        f"silencedetect=noise={noise_db}dB:d={min_dur}", "-f", "null", "-",
    ]
    out = subprocess.run(cmd, capture_output=True, text=True).stderr
    starts = [float(m) for m in re.findall(r"silence_start:\s*([\d.]+)", out)]
    ends = [float(m) for m in re.findall(r"silence_end:\s*([\d.]+)", out)]
    return list(zip(starts, ends))


def duracao(video):
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration",
           "-of", "default=noprint_wrappers=1:nokey=1", video]
    return float(subprocess.run(cmd, capture_output=True, text=True).stdout.strip())


def segmentos_vivos(silencios, dur_total, folga=0.12, min_seg=0.3):
    """Inverte os intervalos de silencio pra obter os trechos falados, com folga."""
    vivos = []
    cursor = 0.0
    for s_ini, s_fim in silencios:
        fim_vivo = min(s_ini + folga, dur_total)
        if fim_vivo - cursor > min_seg:
            vivos.append((cursor, fim_vivo))
        cursor = max(s_fim - folga, fim_vivo)
    if dur_total - cursor > min_seg:
        vivos.append((cursor, dur_total))
    return vivos


def main():
    p = argparse.ArgumentParser()
    p.add_argument("video")
    p.add_argument("--noise-db", type=float, default=-28)
    p.add_argument("--min-dur", type=float, default=0.35)
    p.add_argument("--out-segments", required=True, help="JSON com lista de [ini,fim] a manter")
    args = p.parse_args()

    dur = duracao(args.video)
    silencios = detectar_silencios(args.video, args.noise_db, args.min_dur)
    vivos = segmentos_vivos(silencios, dur)

    with open(args.out_segments, "w") as f:
        json.dump({"duracao_original": dur, "segmentos": vivos}, f, indent=2)

    total_vivo = sum(f - i for i, f in vivos)
    print(f"Duracao original: {dur:.1f}s | silencios: {len(silencios)} | "
          f"segmentos vivos: {len(vivos)} | duracao final: {total_vivo:.1f}s")


if __name__ == "__main__":
    main()
