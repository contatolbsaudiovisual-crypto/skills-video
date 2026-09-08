#!/usr/bin/env python3
"""
Transcricao local do video com faster-whisper (sem envio de dados para fora).
Uso: python3 transcrever.py <video.mp4> [--model small|medium|large-v3] [--out transcricao.json]
"""
import argparse
import json
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("video")
    parser.add_argument("--model", default="small")
    parser.add_argument("--out", default=None)
    args = parser.parse_args()

    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("faster-whisper nao instalado. Rode: pip3 install faster-whisper", file=sys.stderr)
        sys.exit(1)

    model = WhisperModel(args.model, device="auto", compute_type="auto")
    segments, info = model.transcribe(args.video, word_timestamps=True)

    result = {"language": info.language, "segments": []}
    for seg in segments:
        words = [
            {"start": w.start, "end": w.end, "word": w.word}
            for w in (seg.words or [])
        ]
        result["segments"].append({
            "start": seg.start,
            "end": seg.end,
            "text": seg.text.strip(),
            "words": words,
        })

    out_path = args.out or (args.video.rsplit(".", 1)[0] + ".transcricao.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Transcricao salva em: {out_path}")


if __name__ == "__main__":
    main()
