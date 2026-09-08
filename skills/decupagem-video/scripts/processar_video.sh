#!/usr/bin/env bash
# Wrapper genérico: transcreve um vídeo longo e remove silêncios, deixando pronto
# pra etapa de seleção de cortes. Ajuste as variáveis abaixo.
set -euo pipefail

IN="${1:?uso: processar_video.sh <video.mp4>}"
SLUG="$(basename "${IN%.*}" | tr ' ' '-')"
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p tmp

# 1) transcrição local (faster-whisper)
python3 "$DIR/transcrever.py" "$IN" --model small --out "tmp/${SLUG}_transcricao.json"

# 2) (opcional) detectar silêncios pra remoção
python3 "$DIR/cortar_silencio.py" "$IN" --out-segments "tmp/${SLUG}_segmentos.json"

echo "Pronto. Transcrição: tmp/${SLUG}_transcricao.json"
echo "Agora abra a transcrição no Claude e peça os melhores cortes (Passo 3 do SKILL.md)."
