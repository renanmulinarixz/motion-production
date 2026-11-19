---
name: motion-production
description: Criar, revisar e exportar motions com Astra, adaptando direção visual, animação e implementação às ferramentas disponíveis. Usar para logos, tipografia, produto, interfaces, dados e peças narrativas, de qualquer marca ou tema.
---

# Motion Production

Transformar um briefing em motion com direção, continuidade e entrega verificável. Adaptar linguagem, público, marca, duração, formato, som e ferramentas ao projeto. Usar o acervo como repertório; BeSafe é um caso de origem, não o escopo da skill.

## Dirigir e produzir

1. Ler [processo do Astra](references/astra-workflow.md) e [direção](references/direction.md). Definir o efeito pretendido no público, conteúdo exato, formato e resultado editável solicitado. Em revisão, inspecionar a peça atual antes de propor mudanças.
2. Descobrir as ferramentas desta sessão e o acesso real a elas. Usar [adaptações](references/adapters.md) para escolher a rota por controle, editabilidade, estilo, prazo e custo autorizado. Para a rota local, executar `python scripts/capabilities.py`. Um executável encontrado não confirma conexão a editor nem exportação validada.
3. Selecionar referências pelo mecanismo e pela finalidade. Ler [evidências](references/sources.md); abrir poucos quadros pertinentes em `assets/index.html`. Para logos e elementos, consultar [análise por fases](references/logo-elements.md) e `assets/pinterest-logos/index.html`. Materializar os 2.102 frames com `python scripts/prepare_reference_frames.py`; para os 600 frames do modelo, usar `--source model` quando necessário.
4. Planejar os estados importantes, o foco e a ligação entre eles. Usar `assets/brief.example.json` como contrato adaptável e `python scripts/check_brief.py arquivo.json` para verificar seus tempos e IDs. Os [exemplos](references/project-examples.md) demonstram formatos e objetivos diversos. Não impor um número fixo de cenas.
5. Fazer um animatic e resolver a transformação mais incerta. Implementar com as ferramentas escolhidas. Separar conteúdo, estado e apresentação; manter identidade e trajetória das entidades que conectam os beats. Escolher [efeitos](references/effects.md) pelo que acrescentam à ideia.
6. Para Canvas local, adaptar `assets/template/motion.html` em uma pasta do projeto; expor `window.motion.renderAt(t)`, `stateAt(t)`, `duration` e canvas `#stage`. O template é um exemplo de investimentos, não um roteiro universal. Para editores ou outras rotas, preservar o contrato narrativo usando os recursos nativos confirmados.
7. Exportar pela rota disponível e autorizada. Canvas/Chromium: `node scripts/render.cjs fonte.html video.mp4`. Alternativa explícita para Canvas autocontido confiável: `node scripts/render_canvas.cjs fonte.html video.mp4`. Consultar requisitos e limites em [adaptações](references/adapters.md). Esses scripts exportam sem áudio; gravação/síntese, sincronização e mixagem são etapas adicionais quando o projeto inclui som.
8. Rever o vídeo inteiro, tamanho real/reduzido e quadros de fronteira, interação e deformação. Aplicar [qualidade](references/quality.md), corrigir a causa e conferir o arquivo exportado. Na rota local, usar `scripts/check_media.py` com a duração/fps/contagem reais e `scripts/extract_frames.py` para inspeção. Entregar mídia produzida, fonte editável e limitações materiais; preferir arquivo/preview nativo quando disponível.

Resolver caminhos dos scripts a partir da pasta desta skill. Gravar produções na pasta do projeto. Se uma dependência faltar, preservar a fonte e avançar nas etapas independentes; informar qual entrega ainda não foi executada.

## Manter a intenção

- Escolher composição e ritmo pelo público e pela finalidade; não aplicar a estética de uma referência a todos os projetos.
- Fazer a próxima ideia nascer da composição atual quando houver continuidade narrativa. Justificar cortes, trocas de identidade e mudanças reais de assunto.
- Manter foco e hierarquia. Texto, marca ou dado essencial precisa resolver em um estado legível.
- Derivar cursor, máscara e destaque das coordenadas transformadas do alvo em demonstrações de interface.
- Preservar texto, geometria autorizada da marca e significado dos dados. Efeitos não podem contradizer o conteúdo.
- Manter controles de produção fora da imagem final, salvo pedido específico. Não converter um filme em slides por conveniência de implementação.
- Distinguir capacidade documentada, acesso confirmado, execução realizada e resultado aprovado.

## Adaptar sem acoplar

Astra dirige, planeja, implementa e critica a produção; a ferramenta de execução gera os pixels e o arquivo. A mesma intenção pode usar código, editor com camadas, ambiente 3D, geração de assets ou uma combinação.

Consultar [interfaces](references/interfaces.md) para demonstrações de aplicativos e [projetos de origem](references/project-examples.md) para decisões específicas da BeSafe, incluindo sua voz. Uma nova marca define suas próprias escolhas.

Higgsfield é uma rota opcional. Ler [registro de motion nativo](references/higgsfield-native.md) somente se essa rota for pertinente, conferindo capacidades atuais. Para seleção de modelos, benefícios, custos e recuperação de gerações, usar a skill independente `higgsfield-media-production` quando disponível, ou as ferramentas e instruções atuais da plataforma. Preservar a escolha explícita do usuário e o orçamento do projeto.

## Consultar e ampliar

- `assets/pinterest-logos/`: oito fontes, folhas de contato, ZIPs dos frames, fases e PTS no manifesto.
- `assets/model.mp4`, `assets/frames/manifest.json` e `assets/index.html`: modelo próprio de 20 s, 600 frames e catálogo.
- `assets/external-sources.json` e `assets/external/`: 12 registros externos, nove com imagem local.
- [Fontes](references/sources.md): quatro vídeos YouTube tiveram análise automática, sem prints internos disponíveis. Não inventar visualização, autoria ou keyframes.
- [Validação](references/validation.md): distingue testes históricos, inspeção visual amostrada e execução nesta distribuição.

Ao enriquecer o repertório, registrar origem, evidência, mecanismo transferível, implementação possível e critério observável de qualidade. Atualizar o adaptador afetado quando o ambiente mudar; manter decisões de cliente nos exemplos do projeto.
