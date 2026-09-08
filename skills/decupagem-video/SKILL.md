---
name: decupagem-video
description: >
  Decupagem de vídeos longos (aulas, mentorias, lives, YouTube) em cortes curtos para Reels/Shorts/TikTok.
  Recebe um vídeo .mp4 e (quando houver) uma transcrição, encontra os melhores momentos usando um
  sistema de pontuação por gancho/coerência/emoção/valor/desfecho, corta com ffmpeg e queima legenda
  ESTÁTICA (sem animação) na fonte que o usuário passar. Tudo roda local, sem enviar vídeo/áudio
  pra nenhum serviço externo. Use quando o usuário pedir "decupagem", "corta esse vídeo", "tira reels
  desse aulão", "acha os melhores cortes", "transforma essa live em shorts", ou mandar um .mp4 pedindo cortes.
---

# Decupagem de Vídeo (aula/mentoria/YouTube → Reels)

Transforma um vídeo longo em vários cortes curtos prontos pra postar, com legenda estática queimada.
Todo o processamento é local (ffmpeg + Whisper, se necessário) — nenhum arquivo de vídeo/áudio é
enviado para APIs externas.

## Passo 0 — checar dependências (só na primeira vez)

```bash
command -v ffmpeg >/dev/null 2>&1 && echo OK || echo FALTA
```

Se faltar `ffmpeg`:
- Com Homebrew: `brew install ffmpeg`
- Sem Homebrew: pedir pro usuário instalar manualmente (instalação de sistema exige sudo interativo):
  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  brew install ffmpeg
  ```
  Não seguir sem ffmpeg — é pré-requisito pra tudo (corte e legenda).

Se o usuário **não** tiver transcrição com timestamp (ver Passo 1) e pedir pra transcrever aqui, checar Whisper local:
```bash
python3 -c "import faster_whisper" 2>/dev/null && echo OK || echo FALTA
```
Se faltar, instalar sob demanda: `pip3 install faster-whisper` (roda local, modelo baixado uma vez, sem enviar áudio pra fora).

## Passo 1 — receber input

O usuário fornece:
1. **Vídeo**: caminho do `.mp4`
2. **Transcrição** (opcional, varia por vídeo):
   - Com timestamps (`.srt`, `.vtt`, ou JSON tipo Whisper) → usar direto, é o caminho ideal
   - Texto corrido sem tempo → avisar que a precisão do corte vai ser pior (baseada em estimativa de posição no texto), ou oferecer rodar Whisper local pra gerar timestamps reais
   - Nenhuma transcrição → rodar Whisper local (`faster-whisper`, modelo `small` ou `medium` — não precisa do `large-v3`, é custo-benefício ruim pra decupagem)
3. **Fonte da legenda**: perguntar se ainda não foi passada nesta conversa — arquivo `.ttf/.otf` (usuário entrega) ou nome de fonte de sistema. Guardar a escolha, não perguntar de novo dentro do mesmo pedido. (Vem uma fonte livre de exemplo em `fontes/DMSans-Bold.ttf`.)
4. Opcional: quantidade de cortes desejada (padrão: 3-6), duração alvo (padrão: 15-55s), aspect ratio (padrão: 9:16)

Se o vídeo for longo (>40min) e sem transcrição, avisar que o Whisper local pode demorar (CPU: ~1x a 3x a duração do vídeo).

## Passo 2 — transcrever (se necessário)

Só rodar se não veio transcrição com timestamp utilizável. Usar `scripts/transcrever.py` (faster-whisper local, timestamps por palavra). Sem chave de API, sem upload — roda 100% na máquina do usuário.

## Passo 3 — encontrar os melhores cortes

Ler a transcrição completa (com timestamps) e aplicar o sistema de pontuação descrito em
`references/criterios-corte.md`. Resumo do critério (5 dimensões ponderadas, 0-100):

- **Força do gancho** (30%) — abre com afirmação forte, dado contraintuitivo, pergunta que gera curiosidade
- **Coerência isolada** (25%) — faz sentido sozinho, sem precisar do resto do vídeo pra entender
- **Intensidade emocional/opinião** (20%) — trecho com posição forte, virada, exemplo marcante (num aulão isso costuma ser um insight contraintuitivo ou um "erro que todo mundo comete")
- **Densidade de valor** (15%) — ensina algo acionável, dado concreto, passo a passo
- **Qualidade do fechamento** (10%) — fecha com uma frase de impacto, não morre no meio de uma ideia

Duração alvo: 15-55s por corte (ajustar aos limites que o usuário pedir). Sempre alinhar o corte ao **início/fim de frase** (nunca cortar no meio de uma palavra ou ideia) — usar as pausas de fala como fronteira.

Selecionar 8-12 candidatos, pontuar, e apresentar ao usuário os **top 3-6** (ou o número pedido) numa tabela:

> **Cortes sugeridos:**
> | # | Timestamp | Duração | Nota | Por que funciona |
> |---|---|---|---|---|
> | 1 | 12:03–12:41 | 38s | 87 | Abre com dado contraintuitivo sobre X, fecha com virada clara |
> | 2 | ... | ... | ... | ... |
>
> Quer que eu corte todos esses, ajustar algum timestamp, ou já parte pra renderização?

### Passo 3.5 — filtro de encaixe estratégico (quando há contexto de canal)

Nota alta de "vale parar de rolar o feed" **não** decide sozinha. Se o usuário deu contexto do canal
(público-alvo, posicionamento, oferta), passar cada candidato por 4 perguntas antes de apresentar a tabela:

1. **Traz o público certo?** O gancho atrai quem o canal quer como seguidor/lead, ou só curioso genérico? Corte polêmico solto que atrai público errado → rebaixar ou marcar "⚠️ não recomendo".
2. **Bate com o posicionamento?** O corte defende a mesma tese dos vídeos longos? O tom (humor/polêmico/sério) é o tom que o canal já usa?
3. **Abre loop ou entrega tudo de graça?** O melhor corte mostra que existe um método sem ensinar o método inteiro em 40s — deixa a pessoa querendo mais.
4. **Sustenta uma série?** Cortes que seguem um formato recorrente ("erro nº X que todo [público] comete") valem mais que um viral isolado.

Cortes que fisgam o público certo + abrem loop + encaixam em série sobem na prioridade mesmo com nota
um pouco menor. Cortes vetados não somem sozinhos — entram marcados e o usuário decide.

**CHECKPOINT:** esperar aprovação do usuário antes de cortar/renderizar. Ele pode ajustar timestamps manualmente.

## Passo 4 — cortar e queimar legenda

Para cada corte aprovado, usar `scripts/cortar_legendar.py`:

```bash
python3 scripts/cortar_legendar.py video.mp4 --inicio 723 --fim 761 \
  --palavras palavras_do_trecho.json --fonte "Montserrat" \
  [--fontsdir ./fontes] --aspect 9:16 --out cortes/corte-01.mp4
```

`palavras_do_trecho.json` é a lista de palavras com timestamp (start/end/word) daquele trecho,
extraída da transcrição completa gerada no Passo 2 ou fornecida pelo usuário.

O script faz tudo isso automaticamente:
1. Extrai o trecho do mp4 original com ffmpeg
2. Reenquadra para 9:16 (ou o aspect ratio pedido) — crop centralizado por padrão; sem face-tracking (avisar o usuário se ele quiser seguir um rosto e oferecer ajuste manual do `crop` nesse corte)
3. Gera legenda `.ass` a partir dos timestamps por palavra/frase daquele trecho — **sem animação**: texto estático em blocos de 3-8 palavras
4. Usa a fonte informada pelo usuário (`--fonte` + `--fontsdir` se for arquivo custom)
5. Queima a legenda no vídeo com ffmpeg
6. Exporta H.264, otimizado pra Reels/Shorts/TikTok

Ver detalhes de parâmetros em `references/legenda-ass.md`.

## Passo 5 — entregar

Salvar os cortes finais numa pasta `cortes/` ao lado do vídeo original (`corte-01.mp4`, `corte-02.mp4`, etc.).
Mostrar ao usuário a lista de arquivos gerados com timestamp e nota de cada um.

Perguntar se quer legenda de capa/título por cima do corte (texto adicional, não é a legenda falada) — se sim, é outro elemento estático no `.ass`, mesma fonte por padrão a menos que peça diferente.

## Regras

- Nunca enviar o vídeo, áudio ou transcrição pra nenhuma API externa — tudo roda local (ffmpeg + faster-whisper)
- Legenda sempre estática por padrão (sem pop-in, sem karaokê, sem bounce) — só usar animação se o usuário pedir explicitamente
- Sempre alinhar corte a fronteira de frase/pausa natural, nunca no meio de uma palavra
- Sempre mostrar a lista de cortes sugeridos com nota e justificativa antes de renderizar (checkpoint obrigatório)
- Se o usuário já aprovou fonte e estilo antes nesta mesma sessão, não perguntar de novo
- Se faltar ffmpeg, parar e orientar instalação — não tentar workaround sem ele

## Erros conhecidos / aprendizados (ler antes de cortar)

**1. Timestamps da transcrição vs. vídeo bruto — SEMPRE confirmar antes de cortar.**
Se a transcrição foi gerada a partir de um vídeo já editado (ex: cortado no Premiere pra tirar
silêncio/abertura), os timestamps dela NÃO batem com o `.mp4` bruto/original. Cortar o bruto usando
esses timestamps pega o trecho errado. **Antes de cortar, sempre perguntar:** "essa transcrição foi
feita em cima do vídeo bruto que você me passou, ou em cima de uma versão já editada/cortada?" Se for
de uma versão editada, pedir o vídeo editado correspondente, ou calcular o offset exato entre os dois.

**2. Fonte custom (.ttf) pode não casar pelo nome no libass/CoreText.**
Fontes baixadas de CDNs às vezes têm o nome interno de família diferente do nome comercial — ex: um
arquivo "DM Sans Bold" continha internamente o nome de família `DM Sans 9pt` (variante óptica), não
`DM Sans`. O filtro `ass=` do ffmpeg resolve fonte pelo nome de família via CoreText (no macOS) — se
o nome não bater exatamente, cai silenciosamente no fallback do sistema (Helvetica-Bold) sem erro.
**Antes de aplicar em produção:** extrair o nome real da família do arquivo e usar esse nome exato no
`.ass`, ou renderizar um frame de teste e conferir visualmente.

**3. ffmpeg do Homebrew (fórmula padrão) NÃO inclui libass.**
`brew install ffmpeg` sozinho não tem o filtro `ass`/`subtitles` (sem legenda queimada). É preciso
`brew install ffmpeg-full`, que é keg-only — usar via `/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg` ou
colocar esse bin no PATH.

**4. Vídeos 4K/HDR de iPhone são lentos para reencodar.**
Um clipe de ~40s em 4K 10-bit HDR leva ~1-2min pra extrair com libx264. Rodar em background e usar
`-ss` antes do `-i` (input seeking) para acelerar o corte inicial.

**5. Verificar sempre o vídeo original antes de assumir aspect ratio.**
Nem todo vídeo fonte é 16:9 — um vídeo gravado direto em vertical já vem 9:16, dispensando crop.
Rodar `ffprobe -show_entries stream=width,height` antes de montar o filtro de crop.

**6. Sempre entregar um frame de preview antes de considerar o corte "pronto".**
Extrair 1 frame (`ffmpeg -i corte.mp4 -vframes 1 preview.png`) e olhar visualmente — pega erro de
timestamp, fonte errada, ou enquadramento ruim antes de gastar tempo gerando o vídeo inteiro errado.
