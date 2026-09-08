# Legenda estática (.ass) — parâmetros

Formato ASS (Advanced SubStation Alpha), queimado no vídeo via ffmpeg. Estático por padrão:
sem karaokê (`\k`), sem pop-in, sem scale/rotate — cada bloco de frase aparece e some inteiro.

## Estrutura mínima de um .ass estático

```
[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, Outline, Shadow, Alignment, MarginV
Style: Default,<FONTE>,64,&H00FFFFFF,&H00000000,&H80000000,1,3,0,2,120

[Events]
Format: Layer, Start, End, Style, Text
Dialogue: 0,0:00:00.00,0:00:02.50,Default,Texto do primeiro bloco
Dialogue: 0,0:00:02.50,0:00:05.00,Default,Texto do segundo bloco
```

- `Fontname`: nome exato da fonte (se for arquivo `.ttf/.otf` custom, registrar via `fontconfig`
  local ou usar `-vf "subtitles=arquivo.ass:fontsdir=pasta_da_fonte"` no ffmpeg — não precisa
  instalar a fonte no sistema)
- `PrimaryColour`: cor do texto em `&HAABBGGRR` (alpha-blue-green-red, ordem invertida)
- `Alignment`: 2 = centralizado embaixo (padrão pra Reels). Ajustar `MarginV` pra não cair em
  cima da UI da plataforma (zona segura: ~200-250px do fundo em vídeo 1080x1920)
- Sem tags de animação no `Text` (`\t`, `\move`, `\fad` agressivo) — no máximo um fade curto de
  entrada/saída (`\fad(100,100)`, ~100ms) é aceitável e não conta como "animação" perceptível

## Quebra em blocos

Agrupar por frase ou por pausa de fala (não uma legenda por palavra). Bloco ideal: 3-8 palavras,
1-3 segundos na tela, sincronizado com os timestamps reais da transcrição.

## Comando ffmpeg de queima

```bash
ffmpeg -i corte.mp4 -vf "ass=legenda.ass:fontsdir=./fontes" -c:v libx264 -crf 18 -preset medium -c:a aac -b:a 192k saida_final.mp4
```

Se for usar fonte de sistema (nome, sem arquivo), pode omitir `fontsdir` desde que a fonte esteja
instalada no macOS.

## Legenda de capa/título (opcional)

Se o usuário quiser um texto fixo no topo (tipo título do corte), é uma segunda `Style` no mesmo
`.ass` com `Alignment: 8` (topo centralizado) e `Dialogue` cobrindo o corte inteiro (start=0,
end=duração total do corte).
