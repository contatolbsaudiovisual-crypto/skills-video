# Fontes externas — o que trazer, de onde

Varredura no GitHub em 09/09/2026. **Nada entra como está.** Cada repo é matéria-prima para
o `AGENTE.md` do cargo. A Aprimarus é agência de canal (YouTube longo + Reels + redes +
relatório + anúncio); a maioria dos repos é B2B-SaaS-GTM ou marca pessoal — a estrutura
serve, o conteúdo se adapta.

**Aviso sobre estrelas:** a busca do GitHub retorna contagens infladas/fake para vários
desses repos. Julguei por conteúdo, recência e credibilidade do autor, não por ★.

## Ranking dos repos

| Repo | Licença | O que é | Nota | Usar para |
|---|---|---|---|---|
| **gtmagents/gtm-agents** | Apache-2.0 | **67 "plugins" = 67 departamentos**, cada um com ~3 agentes (1 diretor + 2 especialistas) + 3-7 skills. Paid-media, revenue-analytics, revenue-forecasting, pricing-strategy, customer-success, renewal, voice-of-customer, sales (7 plugins), video-marketing, content-marketing, growth-experiments, product-marketing, pr… | 🥇 estrutura | O **modelo de organograma** inteiro. CS, Receitas, Forecast, Growth, Community. Muito sabor enterprise (EBR, deal-desk, ABM) — pegar o esqueleto, não o jargão. |
| **coreyhaines31/marketingskills** | MIT | 51 skills de um marketeiro de SaaS conhecido. `product-marketing.md`-context-first (= nosso `_contexto/`). copywriting, cro, ads, ad-creative, ai-seo, programmatic-seo, seo-audit, analytics, attribution, churn-prevention, pricing, offers, revops, marketing-loops, marketing-psychology, launch, referrals, cold-email, onboarding, marketing-council (multiagente). | 🥇 conteúdo | Estratégia, Conteúdo (copy), Receitas (offers/pricing/revops/loops), CS (churn/onboarding/referrals), SEO. |
| **AgriciDaniel/claude-ads** | ver repo | 34 skills de mídia paga, arquitetura "auditor + conductor", **uma por plataforma**: ads-meta, ads-google, ads-tiktok, ads-youtube, ads-linkedin, ads-reddit, ads-x, ads-pinterest, ads-amazon, ads-apple, ads-microsoft, ads-snapchat + ads-audit/budget/creative/optimize/test/plan/attribution/server-side-tracking/photoshoot/landing/monitor/report. | 🥇 tráfego | **O time de Tráfego Pago quase pronto.** Um cargo por skill. |
| **TheCraigHewitt/skills** | MIT | 65 skills organizadas por **cargo/pasta**: `ceo/`, `sales/`, `youtube/`, `coding/`, `cowork/`, `general/`. YouTube: thumbnail-design, title-craft, description-seo, end-screen-cta, hook-writing, script-structure, retention-editing, channel-strategy, channel-audit, video-analysis, carousels, content-repurpose, content-calendar. CEO: hiring, one-on-ones, financial-review, forecast, negotiation, quarterly-review, delegation. | 🥇 YouTube+gestão | Edição, Design (thumbnail), Conteúdo (roteiro), Diretoria/Gestão. É o mais próximo do nosso negócio (criador). |
| **zubair-trabzada/ai-sales-team-claude** | ver repo | 14 skills: sales-icp, sales-prospect, sales-qualify, sales-outreach, sales-followup, sales-objections, sales-proposal, sales-prep, sales-research, sales-competitors, sales-report. | 🥈 | Comercial/Vendas — qualificador, closer, redator-comercial. |
| **zubair-trabzada/ai-agency-claude** | ver repo | 9 skills de operação de agência: agency-onboard, agency-pipeline, agency-propose, agency-report-pdf, agency-status, agency-client, agency-stack. | 🥈 | Gestão/PMO, CS onboarding, comercial (proposta). |
| **minhnv0807/ai-business-skills** | MIT | 64 SOPs `-global` numerados em 5 packs de cargo + workflows (onboard, monthly-cycle, campaign-launch). | 🥈 | Ciclo mensal, briefs de design, posicionamento, precificação. |
| **postproxy/awesome-marketing-skills** | permissiva | 12 skills discretas: ad-campaigns, campaign-brief, conversion-audit, competitor-pages, email-flows, go-to-market, pricing-plan, product-context, seo-at-scale, ab-test. | 🥈 | conversion-audit (web), ab-test, go-to-market (Receitas). |
| **OneWave-AI/claude-skills** | ver repo | 205 skills grab-bag. Gemas: cash-flow-forecaster, budget-optimizer, churn-autopsy, client-health-dashboard, client-proposal-generator, contract-analyzer/redliner, customer-journey-mapper, board-deck-generator, cowork-invoice-chaser/qbr-builder/sop-writer/hiring-screener. | 🥉 garimpo | Finanças, CS, Jurídico, PMO — pegar arquivos avulsos. |
| **kursku/skills** | ver repo | catálogo PT-BR "+2.300" por categoria. | 🥉 mapa | Jurídico, precificação, categorias que faltam. Qualidade varia muito. |
| **irinabuht12-oss/marketing-skills** · **kostja94/marketing-skills** · **realkimbarrett/advertising-skills** · **AgriciDaniel/claude-seo** | ver repo | coleções de ads/SEO. Segunda leva — checar se a primeira não cobrir. | — | reserva |
| charlie947 / gokepelemo | — | LinkedIn creator / lista de 2020. | descartar (só o checklist CTR já salvo). |

## Times novos — de onde sai cada um

### TRÁFEGO PAGO → base: `AgriciDaniel/claude-ads` (+ minhnv 51-57, gtmagents `paid-media`)
Praticamente 1 cargo por skill do repo. Adaptar: a Aprimarus roda tráfego DO cliente (não
da própria), então o `_contexto/` do cliente injeta conta, verba, meta, pixel.

### RECEITAS → base: gtmagents (`revenue-analytics`, `pricing-strategy`) + coreyhaines (`offers`, `pricing`, `revops`, `marketing-loops`, `referrals`, `free-tools`, `lead-magnets`) + minhnv (`31-offer-design`, `59-go-to-market`)
Time interno da Aprimarus (não opera cliente). Foco: novas linhas de receita — produtizar as
skills, add-ons, parcerias, licenciar o método.

### CUSTOMER SUCCESS → base: gtmagents (`customer-success`, `renewal-orchestration`, `voice-of-customer`, `customer-journey-orchestration`) + coreyhaines (`churn-prevention`, `onboarding`, `referrals`) + minhnv/zubair (`client-onboard`, `agency-onboard`)
Adaptar o vocabulário: lá é "EBR/QBR/renewal ARR"; aqui é "reunião mensal / renovação de
contrato / saúde da conta / humor do cliente no grupo de WhatsApp".

## Regra de importação
1. Ler a skill externa inteira.
2. Extrair só o **método** (passos, checklist, estrutura de entrega) — nunca copiar exemplo,
   nome de cliente ou número.
3. Reescrever no formato `agentes/<cargo>/AGENTE.md` da casa (Ficha de entrada / Ordem de
   leitura / O ofício / Handoffs / O que a versão-cliente injeta / Nunca).
4. Creditar a fonte no rodapé do `AGENTE.md`.

## Não trazer
- E-commerce, dropshipping, "AI avatar", trading/DeFi.
- Qualquer pipeline "escreve prompt → cola no Midjourney/Gemini" — a casa renderiza HTML/CSS.
- Jargão enterprise sem tradução (ARR, ACV, MEDDIC cru) — traduzir pro contexto de agência de criador.
