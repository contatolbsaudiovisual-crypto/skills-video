# Organograma — a produtora como empresa de agentes

Cada **cargo** vira `agentes/<cargo>/AGENTE.md` (ofício genérico, zero dado de cliente).
Depois é replicado como skill dentro de cada cliente / da própria empresa, ganhando identidade,
voz e lista de "nunca" daquele contexto (ver `README.md`). Fontes externas por cargo em
`IMPORTS.md`.

Legenda: **[A]** agente que produz · **[H]** humano no loop · **[A+H]** agente executa /
humano aprova · `ofício` = skill que roda por baixo · *(criar)* = não existe ainda ·
*(fonte: X)* = matéria-prima em repo externo.

---

## 1. DIRETORIA
| Cargo | Faz | Tipo |
|---|---|---|
| `orquestrador` (Jarvis) | recebe pedido, roteia pro cargo, cobra a fila, junta entregas | [A+H] |
| `diretor-de-conteudo` | visão editorial macro entre clientes, padrão de qualidade da casa | [H] |
| `diretor-de-operacoes` | capacidade do time, gargalos, o que a agência aceita e recusa | [A+H] |

## 2. GESTÃO / PMO
| Cargo | Faz | Ofício / fonte |
|---|---|---|
| `gestor-de-projetos` | pedido solto → briefing executável + estrutura de pastas | do Jarvis |
| `coordenador-de-producao` | fila, cotas do plano, prazos, o que está parado e por quê | `operacao/` · *(fonte: minhnv `monthly-cycle`)* |
| `bibliotecario` | mantém `_contexto/`, `agora.md`, ledgers e memória | `consolidate-memory` |

## 3. COMERCIAL / VENDAS
| Cargo | Faz | Ofício / fonte |
|---|---|---|
| `prospector` (SDR) | sourcing de leads no IG, qualifica por ICP, escreve na planilha | `buscador-perfis`, `prospeccao-instagram`, `triagem-instagram` |
| `pesquisador-de-mercado` | ads que rodam no nicho + concorrentes + padrões (Ad Library) | do Jarvis · *(fonte: coreyhaines `competitor-profiling`)* |
| `qualificador-de-leads` | BANT/MEDDIC, prep de call, objeções | *(fonte: zubair `ai-sales-team` sales-qualify/prep/objections)* |
| `closer` | reunião de venda, negociação, fechamento | [H] · *(fonte: TheCraigHewitt `negotiation`, `discovery-call`)* |
| `redator-comercial` | proposta e contrato por plano, follow-up | `contratos/` · *(fonte: zubair `sales-proposal`, OneWave `client-proposal-generator`)* |
| `redator-cold-outbound` | sequência de cold mail / DM de prospecção | *(fonte: coreyhaines `cold-email`, minhnv email)* |

## 4. FINANÇAS
| Cargo | Faz | Ofício / fonte |
|---|---|---|
| `controlador` (CFO) | fluxo de caixa, DRE, saúde financeira | `financas/cfoleo/` · *(fonte: OneWave `cash-flow-forecaster`)* |
| `faturamento` | NFSe Anexo III, cobrança, inadimplência | `reference_nfse_anexo3` · *(fonte: OneWave `cowork-invoice-chaser`)* |
| `forecast` | previsão de receita, variância mês a mês, cenários | *(fonte: gtmagents `revenue-forecasting-pipeline`, TheCraigHewitt `forecast`)* |
| `analista-de-margem` | custo e margem por cliente, rentabilidade da carteira | *(criar)* |

## 5. RECEITAS (novas formas de ganhar dinheiro)
Time que não opera cliente — pensa o modelo de negócio da própria empresa.
| Cargo | Faz | Ofício / fonte |
|---|---|---|
| `head-de-receita` | mapeia fontes de receita atuais e potenciais, prioriza apostas | *(fonte: gtmagents `revenue-analytics`, coreyhaines `revops`, `marketing-loops`)* |
| `desenhista-de-oferta` | monta oferta nova (produto, upsell, add-on, done-with-you) | *(fonte: coreyhaines `offers`, minhnv `31-offer-design`, TheCraigHewitt `proposal-pricing`)* |
| `estrategista-de-preco` | modelo e packaging de planos, reajuste, elasticidade | *(fonte: gtmagents `pricing-strategy`, coreyhaines `pricing`, minhnv `17-pricing`)* |
| `arquiteto-de-produtizacao` | transforma serviço em produto escalável (ex.: as próprias skills como SaaS) | *(fonte: postproxy `go-to-market`, minhnv `59-go-to-market`)* |
| `pesquisador-de-oportunidade` | novos nichos, novos serviços, parcerias, licenciamento | *(fonte: coreyhaines `marketing-ideas`, `co-marketing`, `free-tools`, `lead-magnets`)* |
| `analista-ltv-cac` | LTV, CAC, payback, churn de receita, expansão | *(fonte: gtmagents `revenue-analytics` cohort-analysis, OneWave `churn-autopsy`)* |

## 6. CUSTOMER SUCCESS
Suporte + experiência + retenção dos clientes atendidos.
| Cargo | Faz | Ofício / fonte |
|---|---|---|
| `gerente-de-sucesso` | dono da conta do lado da entrega, plano de sucesso por cliente, reunião mensal | *(fonte: gtmagents `customer-success` adoption-program-manager, minhnv `20-client-intake`)* |
| `onboarding` | primeiros 30 dias de cliente novo: acessos, contexto, calendário, expectativa | *(fonte: minhnv workflow `client-onboard`, zubair `agency-onboard`)* |
| `analista-de-saude-de-conta` | score de saúde por cliente (uso da cota, engajamento, resultado, humor do cliente) | *(fonte: gtmagents `customer-health-director` + `risk-scoring-framework`, OneWave `client-health-dashboard`)* |
| `analista-de-churn` | prevê e ataca risco de cancelamento, plano de recuperação | *(fonte: coreyhaines `churn-prevention`, gtmagents `renewal-orchestration`)* |
| `voz-do-cliente` | coleta e sistematiza feedback, fecha o loop, alimenta o time de Receitas | *(fonte: gtmagents `voice-of-customer`)* |
| `suporte` | dúvida operacional, ajuste pontual, primeira resposta rápida | [A+H] |
| `gestor-de-relacionamento` | reunião de renovação, upsell no momento certo, referral | *(fonte: gtmagents `renewal-director`, coreyhaines `referrals`)* |

## 7. ESTRATÉGIA
| Cargo | Faz | Ofício / fonte |
|---|---|---|
| `estrategista-de-marca` | captura identidade visual real → `marca/tokens.css` + `IDENTIDADE.md` | do Jarvis |
| `estrategista-de-conteudo` | pauta, calendário, ângulo de cada peça, encaixe na esteira | `social-media` · *(fonte: coreyhaines `content-strategy`, minhnv `40-next-content-plan`)* |
| `analista-de-dados` (Growth) | relatório mensal, leitura de métricas, engenharia reversa de padrão | `triagem-instagram` · *(fonte: minhnv `13`/`10`, coreyhaines `analytics`/`attribution`)* |
| `posicionamento` | ICP, oferta, mensagem central, GTM de produto novo do cliente | *(fonte: coreyhaines `product-marketing`/`customer-research`/`marketing-psychology`)* |
| `experimentacao` | hipótese → teste A/B → guardrail → aprendizado | *(fonte: coreyhaines `ab-testing`, gtmagents `growth-experiments`, minhnv `19-ab-test`)* |

## 8. CONTEÚDO (redação)
| Cargo | Faz | Ofício / fonte |
|---|---|---|
| `roteirista-youtube` | roteiro do vídeo longo na voz do cliente | `roteiro-cliente` → `copywriter` · *(fonte: TheCraigHewitt `script-structure`/`hook-writing`)* |
| `roteirista-reels` | roteiro/estrutura de Reel curto (gancho 1,5s) | `copywriter` (formato reel) |
| `storyteller` | conteúdo com história pessoal / vulnerabilidade (IHC) | `metodo-ihc` |
| `copywriter-anuncio` | copy de anúncio estático e em vídeo | `copywriter` · *(fonte: coreyhaines `copywriting`/`ad-creative`)* |
| `copywriter-venda` | página de vendas, VSL, carta (níveis de consciência) | `schwartz-copy` · *(fonte: coreyhaines `offers`/`cro`)* |
| `copywriter-marca` | Big Idea, manifesto, tagline | `ogilvy-copy` |
| `pesquisador-de-pauta` | lê contexto do cliente e traz material antes do roteiro | `roteiro-cliente` |
| `editor-de-copy` | revisa e aperta copy existente sem reescrever a intenção | *(fonte: coreyhaines `copy-editing`)* |

## 9. EDIÇÃO
| Cargo | Faz | Ofício / fonte |
|---|---|---|
| `editor-youtube` | edição do longo: corte por sentido, inserts, ritmo, estilo do canal | *(criar)* · *(fonte: TheCraigHewitt `retention-editing`)* |
| `editor-reels` | take de celular → Reel montado (silêncio, legenda karaokê, B-roll topo) | `montador-reel` |
| `clipador` | vídeo longo → cortes, pontua + filtro de encaixe estratégico | `decupagem-video` |
| `motion-designer` | animações e cartelas (PrintEstudo, CardEstudo, TituloBloco) | `remotion` |
| `legendista` | legenda queimada `.ass`, karaokê, ortografia BR | parte de `editor-reels`/`clipador` |
| `broll-researcher` | busca B-roll (TikTok > stock > Magnific), sempre vídeo | `feedback_broll_origem_tiktok` |
| `editor-audio` | limpeza, mixagem, SFX, níveis | parte de `montador-reel` |
| `dublador` | dublagem / legendagem multi-idioma | Magnific `video_dubbing` |
| `finalizador` | color, master, checagem de export (codec, HDR/SDR, dimensão) | preset por canal |

## 10. DESIGN
| Cargo | Faz | Ofício / fonte |
|---|---|---|
| `diretor-de-arte` | define formato e hierarquia visual da peça antes de produzir | *(fonte: minhnv `30-design-master`/`48`, gtmagents `design-creative`)* |
| `designer-thumbnail` | thumbnail 1280x720 no estilo do canal | *(criar)* · *(fonte: TheCraigHewitt `thumbnail-design`+`title-craft`, charlie947 checklist)* |
| `designer-carrossel` | carrossel Instagram | `carrossel` |
| `designer-anuncio` | anúncio estático (feed/stories) | *(criar)* · *(fonte: Jarvis `designer`, minhnv `42-image-brief`)* |
| `web-designer` | página de captura / vendas (HTML+CSS, 1 arquivo) | do Jarvis · *(fonte: postproxy `conversion-audit`, minhnv `12`)* |
| `retocador` | recorte, upscale, relight, remoção de fundo | Magnific `images_*` |
| `designer-identidade` | brand guideline quando o cliente não tem marca | *(fonte: minhnv `46-brand-guideline`)* |

## 11. SOCIAL MEDIA / DISTRIBUIÇÃO
| Cargo | Faz | Ofício / fonte |
|---|---|---|
| `social-media-strategist` | calendário editorial, repurposing (1 vídeo → N posts) | `social-media` · *(fonte: TheCraigHewitt `content-repurpose`/`content-calendar`)* |
| `publicador` | publica IG/TikTok/FB/LinkedIn/Threads/blog, cada um no formato próprio | `repurpose-conteudo`, `publicar-instagram` |
| `community-manager` | rotina de engajamento, responde comentários no tom do cliente | `vidiq_generate_comment_replies` · *(fonte: gtmagents `community-building`)* |
| `social-listening` | monitora menções, concorrentes, sentimento | *(fonte: minhnv `15-social-listening`, gtmagents `voice-of-customer`)* |

## 12. TRÁFEGO PAGO
Time dedicado — anúncio pago é entrega de vários planos e alguns planos incluem volume "ilimitado".
| Cargo | Faz | Ofício / fonte |
|---|---|---|
| `head-de-trafego` | plano de mídia, verba por canal, meta de CPA/ROAS, leitura semanal | *(fonte: AgriciDaniel `ads`/`ads-plan`/`ads-budget`, gtmagents `paid-media` media-strategist)* |
| `gestor-meta` | campanha Meta (Facebook/Instagram/Advantage+), públicos, estrutura de conta | *(fonte: AgriciDaniel `ads-meta`)* |
| `gestor-google` | Google Search/PMax/YouTube Ads | *(fonte: AgriciDaniel `ads-google`/`ads-youtube`)* |
| `gestor-tiktok` | TikTok Ads | *(fonte: AgriciDaniel `ads-tiktok`)* |
| `analista-de-criativos-pagos` | testa e itera criativo pago, mata fadiga, feeds do designer-anuncio | *(fonte: AgriciDaniel `ads-creative`/`ads-test`, minhnv `55-scaling-ads`)* |
| `especialista-tracking` | Pixel/CAPI, GTM, UTM, tracking server-side, atribuição | *(fonte: AgriciDaniel `ads-server-side-tracking`/`ads-attribution`, minhnv `53-tracking-setup`)* |
| `otimizador` | ajuste de lance/verba, escala, corte, realocação | *(fonte: AgriciDaniel `ads-optimize`/`ads-monitor`, minhnv `55`/`56`)* |
| `auditor-de-contas-pagas` | auditoria de conta de anúncio (do cliente ou nova) | *(fonte: AgriciDaniel `ads-audit`, minhnv `21-ads-audit`)* |

## 13. TI / DEV
| Cargo | Faz | Ofício / fonte |
|---|---|---|
| `devops` | Cloudflare, DNS, backup GitHub, hooks, segurança da conta | memórias de infra |
| `dev-automacao` | scripts de apoio (chrome-helper, rodízio Apify, geradores de arte) | `scripts/` |
| `dev-plataforma` | mantém o próprio `agentes/`, cria e versiona skills | `skill-creator` |
| `integracoes` | conectores: Magnific, vidIQ, Apify, Google, Meta | `.mcp.json` |
| `seguranca` | revisão de segurança de código e de dados sensíveis | `security-review`, `claude-security` |

## 14. TRANSVERSAL
**Todo time tem um revisor próprio.** `agentes/revisor/AGENTE.md` é a doutrina (julga, não
corrige; checks objetivos + rubrica 1-5; 3 vereditos; parecer em arquivo; regra dos três).
Cada time herda e traz a própria lista de checks:
| Cargo | Audita | Herda |
|---|---|---|
| `revisor-conteudo` | roteiro, copy, legenda, manifesto | `revisor` (= `revisor-geral`) |
| `revisor-design` | thumbnail, carrossel, anúncio, página | `revisor` + minhnv `47-design-review` |
| `revisor-edicao` | vídeo longo, Reel, corte, motion (com timecodes) | `revisor` + TheCraigHewitt `video-analysis` |
| `revisor-trafego` | plano de mídia, conta, criativo pago, tracking, QUALQUER mudança (trava veiculação) | `revisor` + claude-ads mutation gate |
| `revisor-seo` | título, descrição, tags, capítulos, frase-gancho (checklist vidIQ) | `revisor` |
| `revisor-social` | legenda, pacote de posts, agendamento (POSICOES-FIXAS) — último portão antes do ar | `revisor` |
| `juridico` | contrato, direito de imagem, LGPD, termos | *(fonte: kursku `juridico-compliance`)* |

---

---

## Prioridade de construção (sugestão)

1. **Buracos que costumam doer primeiro:** `designer-thumbnail`, `designer-anuncio`, `editor-youtube`, `diretor-de-arte`.
2. **Fundação do fluxo:** `gestor-de-projetos`, `estrategista-de-marca`, `pesquisador-de-mercado`.
3. **Recorrente de conteúdo:** roteiristas, `seo-youtube`, `clipador`, `editor-reels` — em geral só o adaptador fino (o ofício já existe numa skill).
4. **Times de negócio:** Tráfego Pago (importar a suíte `AgriciDaniel/claude-ads`), Customer Success, Receitas.
5. **Gestão e números:** `analista-de-dados`, `coordenador-de-producao`, `forecast`.

## Como usar

- `agentes/<cargo>/AGENTE.md` é o **ofício genérico** — mexer aqui, não em N pastas de cliente.
- Cada negócio/cliente ganha um **adaptador fino** que aponta pro `AGENTE.md` e injeta só a
  exclusividade (identidade visual, voz, esteira de produtos, lista de "nunca").
- Todo time tem **revisor próprio** — a doutrina em `agentes/revisor/`, os checks por time em `revisor-<time>/`.
