---
name: roteiro
description: Cria roteiro de vídeo (ou ideia/pauta/título) para um canal, seguindo o modelo de roteiro, temas já gravados, tom de voz e CTA daquele canal. Use quando o usuário pedir "roteiro", "ideia de vídeo", "pauta", "tema pro vídeo", "título".
---

# Roteiro de Vídeo

## Passo 1 — identificar o canal

Se não estiver claro no pedido, perguntar: é para qual canal? Manter uma pasta por canal com o
contexto (ex: `canais/<nome>/`).

## Passo 2 — ler o contexto antes de escrever

Sempre ler, na pasta do canal:
1. `contexto.md` — quem é, nicho, tom, CTA padrão
2. `modelo-e-temas.md` — estrutura de roteiro testada, banco de temas, temas já gravados (não repetir)
3. Se existir, pesquisa de público/concorrentes — usar pra calibrar gancho/ângulo/CTA, não usar dado genérico de mercado quando existir dado real do canal

## Passo 3 — escrever o roteiro

Seguir exatamente a estrutura documentada em `modelo-e-temas.md` daquele canal (cada um tem formato
próprio de título/thumbnail/gancho/CTA). Não usar um formato genérico só porque é mais rápido — a
estrutura por canal existe porque já foi validada.

Verificar se o tema pedido já está na lista de "temas já gravados" — se estiver, avisar antes de prosseguir.

## Passo 4 — revisão geral (obrigatório)

Antes de entregar, invocar a skill `revisor-geral` sobre o roteiro final. Se ela reprovar algum ponto,
ajustar e entregar já revisado.

## Passo 5 — descrição do vídeo (quando pedido)

Se o pedido incluir a descrição do YouTube (não confundir com SEO de canal — isso é a skill
`youtube-seo-canal`), seguir o template do canal, se existir. Senão: keyword principal nos primeiros
150-200 caracteres, resumo curto, capítulos/timestamps (vídeos acima de 10min), CTA único, bloco de
links separado (nunca `@handle` solto no texto), 3-5 hashtags no final.

## Passo 6 — registrar

Depois de entregar, perguntar se deve adicionar o tema à lista de "temas já gravados" em `modelo-e-temas.md`.
