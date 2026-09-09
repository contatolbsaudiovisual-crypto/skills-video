# Skills e organograma de agentes (Claude Code)

Dois blocos, **sem nenhum dado de cliente, conta ou pessoa**:

- **`agentes/`** — organograma completo de uma produtora de conteúdo como empresa de agentes:
  **86 cargos** genéricos (o *ofício* de cada função), organizados em 14 times. Ver
  `agentes/README.md` para o modelo de 3 níveis e `agentes/ORGANOGRAMA.md` para o quadro.
- **`skills/`** — skills de Claude Code prontas de produção de vídeo. Cada pasta é uma skill
  independente (`/decupagem-video`, `/social-media`, …).

---

## `agentes/` — organograma de cargos

O modelo (detalhe em `agentes/README.md`):

```
skill/playbook          ← o OFÍCIO: como se faz o trabalho (copywriter, decupagem, seo…)
agentes/<cargo>/AGENTE.md ← o CARGO: o que entrega, o que NÃO faz, de quem recebe / pra quem
                           passa, qual ofício usa, e "o que a versão-cliente injeta"
adaptador fino           ← a PESSOA no cargo, de um cliente/empresa: aponta pro AGENTE.md e
                           injeta só a exclusividade (identidade visual, voz, esteira, "nunca")
```

**Regra:** o ofício mora num lugar só. Muda em `agentes/<cargo>/` — não em N pastas de cliente.

### Os 14 times
Diretoria · Gestão/PMO · Comercial · Finanças · **Receitas** · **Customer Success** ·
Estratégia · Conteúdo · Edição · Design · Social/Distribuição · **Tráfego Pago** · TI/Dev ·
Revisão (**um revisor por time**) + Jurídico.

- `agentes/ORGANOGRAMA.md` — o quadro de cargos por time, com o que cada um entrega e a fonte.
- `agentes/IMPORTS.md` — mapa do que dá pra puxar de repositórios externos de skills, por cargo
  (gtmagents, coreyhaines31/marketingskills, AgriciDaniel/claude-ads, TheCraigHewitt/skills,
  minhnv0807/ai-business-skills, postproxy). Regra: extrair só o método, reescrever no formato
  da casa, creditar.

Estrutura inspirada no Jarvis OS (sistema irmão). Paths que citam `Aprimarus/…`,
`.claude/skills/…` ou `project_…` de memória são **exemplos** do sistema de origem — troque
pelos do seu.

---

## `skills/` — como instalar

```bash
git clone <url-deste-repo> skills-video
cp -R skills-video/skills/* ~/.claude/skills/     # global
# ou: cp -R skills-video/skills/* <seu-projeto>/.claude/skills/
```

Reinicie o Claude Code. As skills aparecem sozinhas.

| Skill | Pra que serve |
|---|---|
| **`decupagem-video`** | Vídeo longo → cortes curtos. Pontua os melhores momentos, corta com ffmpeg, queima legenda. **100% local.** |
| **`social-media`** | Calendário editorial, repurposing (1 vídeo → vários posts), rotina de engajamento. Não escreve o texto final. |
| **`roteiro`** | Roteiro / pauta / título seguindo o modelo, tom e CTA de cada canal. |
| **`youtube-seo-canal`** | SEO da página "Sobre", palavras-chave, banco de tags, links. |
| **`revisor-geral`** | Auditoria final de qualquer texto pronto pra publicar. Aponta, não reescreve. |

### Dependências da `decupagem-video`
- `ffmpeg` **com libass** — macOS: `brew install ffmpeg-full`
- `python3` · `faster-whisper` (só se transcrever aqui): `pip3 install faster-whisper`

### Notas
- `skills/decupagem-video/fontes/DMSans-Bold.ttf` (SIL Open Font) é só exemplo de legenda — troque pela fonte da sua marca.
- `revisor-geral` e `roteiro` esperam um documento de contexto/tom de voz por canal — crie o seu.
- Skills de publicação automática (Instagram/TikTok/LinkedIn) ficaram de fora: dependem de credenciais e apps por conta.

---

## Catálogo de outras skills de vídeo (referência, não incluídas)

- **video-use** (`github.com/browser-use/video-use`) — corte por transcrição, detecta silêncios.
- **video-editing-skill** (`github.com/6missedcalls/video-editing-skill`) — Bash + FFmpeg + Whisper, local.
- **Remotion skill** (`remotion-dev/skills`) — React → MP4, motion graphics.
- **HeyGen** (`heygen-com/skills`) — avatar falante multilíngue.
- **claude-watch** / **claude-video** — Claude "assiste" um vídeo.
