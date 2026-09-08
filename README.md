# Skills de edição / conteúdo de vídeo (Claude Code)

Conjunto de skills de Claude Code para produção de conteúdo de vídeo, sem nenhum dado de cliente,
conta ou pessoa. Cada pasta em `skills/` é uma skill independente.

## Como instalar

Copie as pastas de `skills/` para uma dessas localizações:

- **Global (todos os projetos):** `~/.claude/skills/`
- **Por projeto:** `<seu-projeto>/.claude/skills/`

```bash
git clone <url-deste-repo> skills-video
cp -R skills-video/skills/* ~/.claude/skills/
```

Reinicie o Claude Code. As skills aparecem sozinhas — chame com `/decupagem-video`, `/social-media`, etc.

## O que tem aqui

| Skill | Pra que serve |
|---|---|
| **`decupagem-video`** | Vídeo longo (aula/live/YouTube) → cortes curtos pra Reels/Shorts/TikTok. Pontua os melhores momentos (gancho/coerência/emoção/valor/fechamento), corta com ffmpeg e queima legenda estática. **Roda 100% local** — nada sai da máquina. |
| **`social-media`** | Planejamento: calendário editorial, repurposing (1 vídeo → vários posts), rotina de engajamento, engenharia reversa de padrão que funciona. Não escreve o texto final. |
| **`roteiro`** | Roteiro / pauta / título de vídeo seguindo o modelo, tom e CTA de cada canal (uma pasta de contexto por canal). |
| **`youtube-seo-canal`** | SEO da página "Sobre" do canal, palavras-chave, banco de tags, links. Pesquisa antes de escrever. |
| **`revisor-geral`** | Auditoria final de qualquer texto pronto pra publicar (regras de linguagem, tom, coerência com o pedido). Aponta, não reescreve. |

## Dependências da `decupagem-video`

- `ffmpeg` **com libass** — no macOS: `brew install ffmpeg-full` (a fórmula `ffmpeg` padrão não tem legenda queimada)
- `python3`
- `faster-whisper` (só se for transcrever aqui): `pip3 install faster-whisper`

## Notas

- `skills/decupagem-video/fontes/DMSans-Bold.ttf` é a fonte DM Sans (licença SIL Open Font), incluída
  só como exemplo de legenda. Troque pela fonte da sua marca.
- `revisor-geral` e `roteiro` esperam um documento de contexto/tom de voz por canal — crie o seu.
- Skills de publicação automática em redes (Instagram/TikTok/LinkedIn) ficaram de fora de propósito:
  dependem de credenciais e apps registrados que são específicos de cada conta.

## Catálogo de outras skills de vídeo (não incluídas, referência)

Não estão neste repo, mas valem pesquisa:

- **video-use** (`github.com/browser-use/video-use`) — corte por transcrição, detecta silêncios/respirações, propõe estratégia antes de aplicar.
- **video-editing-skill** (`github.com/6missedcalls/video-editing-skill`) — Bash + FFmpeg + Whisper, 100% local. Trim, jump cut, legenda estilo Hormozi, remoção de silêncio.
- **Remotion skill** (`remotion-dev/skills`) — componentes React compilados em MP4. Motion graphics, lower-thirds, data viz animada. Não gera footage realista.
- **HeyGen** (`heygen-com/skills`) — avatar falante multilíngue.
- **claude-watch** / **claude-video** — Claude "assiste" um vídeo: frames + transcrição + análise de gancho.
- **seek-and-analyze-video** — busca vídeos e analisa o que viraliza num nicho.
