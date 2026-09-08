---
name: social-media
description: Planeja calendário editorial de redes sociais, transforma conteúdo longo (vídeo, roteiro, live) em vários posts curtos (repurposing), organiza rotina de engajamento, e faz reverse engineering de padrões que já performaram num nicho. Use quando o usuário pedir "calendário de postagem", "o que postar essa semana", "transformar esse vídeo em posts", "repurposing", "rotina de engajamento". Para ESCREVER o texto final, usar uma skill de copy — esta skill organiza o quê e quando, não escreve o texto. Framework adaptado de coreyhaines31/marketingskills.
---

# Social Media (planejamento e sistema)

Esta skill cuida do **sistema**: o que postar, quando, e como espremer mais posts de um conteúdo já
produzido. Para escrever o texto final do post/roteiro, usar a skill de copy do projeto — não duplicar aqui.

## Passo 1 — contexto

Ler o documento de contexto do canal (persona, tom, CTA), os pilares de conteúdo, e a cadência
vigente — não sugerir calendário fora do que o canal cobre.

## Calendário editorial semanal

Modelo de referência (adaptar pilares e dias ao canal específico, não usar genérico):

| Dia | Formato | Pilar |
|---|---|---|
| Seg | Reel educativo | rotativo entre os pilares do canal |
| Ter | Carrossel | pilar de autoridade/prova |
| Qua | Reel de reação/tendência | notícia recente do nicho |
| Qui | Reel tela dividida ou lista | pilar prático/tutorial |
| Sex | Bastidor/autoridade | replicar formato que já validou bem no perfil |

Batching: reservar um bloco (2-3h) por semana pra escrever vários roteiros de uma vez em vez de um
por dia — reduz troca de contexto e mantém consistência de tom.

## Repurposing (1 conteúdo → vários posts)

Todo conteúdo longo (aula, live, masterclass gravada) rende vários formatos curtos. Antes de gravar
algo novo, checar se dá pra extrair "átomos de conteúdo" de algo que já existe:

| Tipo de átomo | O que procurar | Formato de saída |
|---|---|---|
| Frase marcante | Afirmação forte, opinião direta, frase que resume tudo (15-60s) | Reel curto, carrossel de citação |
| História completa | Mini-narrativa com início, conflito, resolução (60-90s) | Reel de storytelling |
| Dica tática | Passo a passo específico e claro (30-60s) | Reel lista, carrossel tutorial |
| Opinião contrária | Discorda de algo comum no nicho | Reel de reação |
| Dado/número surpreendente | Estatística que choca ou surpreende | Carrossel, reel gancho numérico |
| Bastidor | Momento real, não roteirizado | Reel bastidor/autoridade |

Fluxo:
1. Pegar transcrição do conteúdo longo (se não tiver, gerar a partir do vídeo ou do roteiro já escrito)
2. Marcar 5-10 melhores momentos
3. Pra cada um, definir o átomo e o formato de saída (tabela acima)
4. Escrever cada post como se funcionasse sozinho, sem depender de quem viu o conteúdo original
5. Distribuir ao longo de 1-2 semanas, não postar tudo junto

> Dica: a skill `decupagem-video` faz o passo 1-2 automático quando o conteúdo longo é um vídeo.

## Rotina de engajamento

Rotina diária curta, não escalável em massa (nunca automatizar comentário/DM — engajamento fake é
detectável e prejudica a conta):
1. Responder todos os comentários dos posts recentes
2. Comentar em 5-10 posts de perfis de referência do nicho (não concorrente hostil, perfis que constroem relação)
3. Compartilhar/repostar algo relevante com um comentário próprio agregando valor
4. Comentário de qualidade: adicionar algo novo, não "ótimo post!" — compartilhar experiência própria ou pergunta genuína

## Reverse engineering de padrão (codificar o que já funciona)

1. Levantar posts de maior desempenho (do próprio canal e de referências do nicho)
2. Identificar o que se repete: gancho, formato, duração, CTA
3. Documentar o padrão
4. Aplicar o padrão com a voz/tom do canal, nunca copiar frase a frase de outro perfil

## Métricas que importam (pra revisão semanal, não pra decidir cada post isoladamente)

- **Alcance**: impressões, contas alcançadas, taxa de crescimento de seguidores
- **Engajamento**: taxa de engajamento, comentários (vale mais que curtida), compartilhamentos, salvamentos
- **Conversão**: cliques no link, visitas ao perfil, mensagens diretas recebidas, leads atribuídos

Revisão semanal: os 3 posts que mais performaram e por quê, os 3 piores e o que mudar, tendência de
crescimento de seguidor, melhor horário de postagem (baseado em dado real, não suposição genérica).

## Quando o engajamento cai

- Testar novo gancho / outro horário / outro formato (ex: trocar carrossel por reel)
- Aumentar engajamento ativo em outros perfis (rotina acima)

Quando o alcance cai:
- Evitar link externo no corpo do post (prejudica alcance orgânico)
- Aumentar frequência de postagem
- Engajar mais em comentários
- Testar mais vídeo/visual
