# `agentes/` — biblioteca de cargos (genérica)

- **`ORGANOGRAMA.md`** — o quadro completo de cargos por departamento/time (diretoria, gestão,
  comercial, finanças, estratégia, conteúdo, edição, design, social, TI). Ponto de partida.
- **`IMPORTS.md`** — o que trazer de repositórios externos de skills, por cargo.
- Este arquivo — como os três níveis (ofício / cargo / pessoa-no-cliente) se encaixam.

Esta pasta é o **RH genérico**. Cada subpasta é um **cargo** — a descrição bruta de um ofício,
escrita **sem dado de nenhum cliente**. É a programação-base que depois é **replicada** para
dentro de cada cliente (ou da própria empresa), onde ganha a exclusividade: identidade
visual, voz, esteira de produtos, lista de "nunca".

## Como os três níveis se encaixam

```
.claude/skills/            ← os OFÍCIOS (motores de craft): copywriter, carrossel,
                              decupagem-video, youtube-seo-canal, revisor-geral, repurpose-conteudo...
                              Sabem COMO fazer. Não sabem para quem.

agentes/<cargo>/AGENTE.md  ← os CARGOS (este diretório): roteirista, seo-youtube,
                              designer-thumbnail, analista...
                              Enquadram o papel: o que o cargo entrega, o que NÃO faz,
                              de quem recebe e para quem passa, e QUAL ofício ele usa.
                              Para os cargos sem motor pronto (thumbnail, anúncio, edição,
                              análise, página), o craft está escrito aqui mesmo.

Clientes/<slug>/.claude/skills/<slug>-<cargo>/SKILL.md   ← a PESSOA no cargo, deste cliente.
Aprimarus/.claude/skills/aprimarus-<cargo>/SKILL.md        Arquivo curto (~20-40 linhas):
                              "siga agentes/<cargo>/AGENTE.md" + os ponteiros de contexto
                              do cliente + a lista de "nunca" dele + as injeções de marca.
```

Regra: **o ofício mora em um lugar só.** Se a forma de escrever roteiro muda, muda em
`agentes/roteirista/` — não em N pastas de cliente. A pasta do cliente só carrega o que é
exclusivo dele.

**Todo time tem revisor próprio.** `agentes/revisor/AGENTE.md` é a doutrina; `revisor-conteudo`,
`revisor-design`, `revisor-edicao`, `revisor-trafego`, `revisor-seo` e `revisor-social`
herdam dela e trazem a lista de checks do time. O cliente replica um `revisor-<time>` para
cada time ativo na conta dele.

## O quadro de cargos

### Fundação — rodam 1x no onboarding do cliente, não recorrente
| Cargo | Entrega |
|---|---|
| `gestor-de-projetos` | pedido solto → briefing executável + estrutura de pastas |
| `pesquisador-de-mercado` | anúncios que rodam no nicho + concorrentes + padrões (Ad Library Meta) |
| `estrategista-de-marca` | captura a identidade visual real do expert → `marca/tokens.css` + `IDENTIDADE.md` |

### Conteúdo — recorrente
| Cargo | Entrega | Ofício por baixo |
|---|---|---|
| `estrategista-de-conteudo` | pauta, calendário editorial, ângulo de cada peça, encaixe na esteira | `social-media` |
| `roteirista` | roteiro de vídeo (longo e Reel) na voz do cliente | `roteiro-cliente` → `copywriter` / `metodo-ihc` |
| `editor-youtube` | edição do vídeo longo no estilo do canal | craft aqui |
| `editor-reels` | take bruto de celular → Reel montado | `montador-reel` |
| `clipador` | vídeo longo → cortes para Reels/Shorts/TikTok | `decupagem-video` |

### Distribuição — recorrente
| Cargo | Entrega | Ofício por baixo |
|---|---|---|
| `seo-youtube` | título, descrição, tags, capítulos, copy de thumb | `youtube-seo-canal` + checklist vidIQ |
| `social-media` | publicação multiplataforma (IG/TikTok/Threads/LinkedIn/blog), legendas, posições fixas | `repurpose-conteudo` / `publicar-instagram` |
| `analista` | relatório mensal, leitura de métricas, preparação de reunião | craft aqui |

### Design — recorrente
| Cargo | Entrega | Ofício por baixo |
|---|---|---|
| `designer-thumbnail` | thumbnail 1280x720 no estilo do canal | craft aqui (HTML/CSS→Chrome ou PIL) |
| `designer-carrossel` | carrossel Instagram | `carrossel` |
| `designer-anuncio` | anúncio estático (feed/stories) | craft aqui (HTML/CSS→Chrome) |
| `web-designer` | página de captura ou vendas (HTML+CSS, 1 arquivo) | craft aqui |

### Transversal
| Cargo | Entrega |
|---|---|
| `revisor` | audita a entrega contra o briefing e as regras da casa. Aprova ou aponta, nunca reescreve. Roda por último. |

## Como replicar um cargo para um cliente

1. Crie `Clientes/<slug>/.claude/skills/<slug>-<cargo>/SKILL.md`.
2. Corpo (curto):
   ```markdown
   ---
   name: <slug>-<cargo>
   description: <Cargo> do <Cliente>. <1 linha do que faz e quando disparar>.
   ---
   # <Cargo> — <Cliente>

   O ofício está em `../../../../agentes/<cargo>/AGENTE.md` — siga de lá.

   ## Contexto obrigatório deste cliente
   - `../../_contexto/cliente.md`, `_contexto/voz.md`, `_contexto/agora.md`, `_contexto/provas.md`
   - <arquivos específicos do cargo: modelo-e-temas, _estilo-thumbs-canal, checklist-seo...>

   ## Injeções (a exclusividade deste cliente)
   - **Identidade visual:** <tokens / paleta / fonte, ou "ver marca/tokens.css">
   - **Voz e ganchos:** <o essencial + apontar voz.md>
   - **Esteira / ICP:** <produtos e para quem, ou apontar cliente.md>
   - **Formato/estilo:** <o que é fixo neste canal>

   ## Nunca (deste cliente)
   - <as proibições específicas — clickbait, expor o "sistema", termo X...>
   ```
3. Só entra a exclusividade. Nada de reescrever o ofício.

## Origem

Estrutura inspirada no Jarvis OS do irmão do dono
(`Aprimarus/estrategia/referencias/jarvis-os-2026-09-07/`). Os cargos de fundação
(`gestor-de-projetos`, `pesquisador-de-mercado`, `estrategista-de-marca`) e `web-designer` /
`designer-anuncio` vêm de lá, adaptados: o Jarvis é focado em anúncio+página de lançamento;
o sistema de origem é agência de canal (YouTube longo + Reels + redes + relatório).


## Paths de exemplo

Alguns `AGENTE.md` citam caminhos do sistema de origem (`Aprimarus/templates/...`, `.claude/skills/...`, `project_...` de memória) como **ilustração** de onde aquele insumo mora na casa que gerou isto. Ao adotar, troque pelos caminhos do seu próprio sistema — o método é o que importa, não o path.
