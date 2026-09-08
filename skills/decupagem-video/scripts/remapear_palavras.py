#!/usr/bin/env python3
"""Remapeia timestamps de palavras do eixo de tempo original pro eixo do video
cortado (apos remocao dos silencios), descartando palavras que caem fora dos
segmentos mantidos."""
import argparse
import json


def mapear(t, segmentos):
    """Retorna o tempo remapeado, ou None se t cair num trecho removido."""
    offset = 0.0
    for ini, fim in segmentos:
        if ini <= t <= fim:
            return offset + (t - ini)
        if t < ini:
            return None
        offset += fim - ini
    return None


def main():
    p = argparse.ArgumentParser()
    p.add_argument("palavras_json")
    p.add_argument("segmentos_json")
    p.add_argument("--out", required=True)
    args = p.parse_args()

    with open(args.palavras_json, encoding="utf-8") as f:
        palavras = json.load(f)
    with open(args.segmentos_json, encoding="utf-8") as f:
        seg_data = json.load(f)
    segmentos = seg_data["segmentos"]

    novas = []
    for w in palavras:
        ns = mapear(w["start"], segmentos)
        ne = mapear(w["end"], segmentos)
        if ns is None or ne is None:
            continue
        novas.append({"start": ns, "end": ne, "word": w["word"]})

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(novas, f, ensure_ascii=False)
    print(f"{len(novas)}/{len(palavras)} palavras mantidas apos corte de silencio")


if __name__ == "__main__":
    main()
