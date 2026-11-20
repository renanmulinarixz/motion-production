# Motion Production

Uma skill para o Astra dirigir, construir e revisar motions de diferentes estilos com as ferramentas realmente disponíveis no ambiente.

O processo liga intenção, composição, movimento e entrega. Serve a identidades de marca, logos, tipografia cinética, vídeos de produto, demonstrações de interfaces, visualização de dados, peças editoriais e educativas. A marca, o assunto, a duração, a voz e a ferramenta são definidos pelo projeto.

## O que o Astra passa a fazer

1. Interpretar o briefing e escolher uma linguagem visual apropriada ao público e à finalidade.
2. Transformar referências em decisões de ritmo, geometria, hierarquia e continuidade.
3. Verificar ferramentas, acesso, formatos e dependências antes de escolher a implementação.
4. Planejar os estados importantes e a ligação entre eles; construir um animatic antes de investir no acabamento.
5. Implementar e revisar mantendo os elementos, textos e decisões aprovados.
6. Conferir o arquivo exportado e entregar a mídia, a fonte editável e os limites reais da execução.

A melhoria do Astra vem desse processo, dos exemplos, dos critérios de revisão e dos recursos executáveis que a skill fornece. As capacidades de cada editor ou serviço são verificadas durante a tarefa.

## A rota acompanha o projeto

| Necessidade | Rota a considerar quando disponível |
| --- | --- |
| Tipografia, UI, gráficos e timings exatos | HTML/Canvas/SVG, Remotion ou editor com camadas |
| Composição e animação editáveis em Adobe | After Effects; Premiere para montagem, áudio e legendas |
| Objetos 3D, materiais, câmera e luz | Blender ou outro ambiente 3D acessível |
| Quadros de estilo e preparação de assets | Ferramentas de design ou geração autorizadas |
| Texturas, personagens e trechos orgânicos | Geração de imagens/vídeos integrada a uma composição controlada |
| Um pedido explícito de ferramenta | Preservar a escolha e conferir suas capacidades atuais |

A tabela orienta decisões; não declara essas ferramentas instaladas ou conectadas. Uma rota pode combinar ferramentas, com responsabilidades e arquivos de passagem definidos.

## Uso

Consulte o [atlas visual comentado](skills/motion-production/references/atlas-visual/README.md) para escolher uma referência de abertura, logotipo, gesto de interface ou transição. Cada ficha reúne uma amostra visual, a fonte e uma maneira de aplicar o mecanismo em outra peça.

```text
Use $motion-production para criar uma vinheta de uma marca de café.
Quero formas orgânicas, lettering legível e um loop de 6 segundos.
Escolha a implementação pelas ferramentas disponíveis e entregue a fonte editável.
```

```text
Use $motion-production para um vídeo vertical de lançamento de aplicativo.
Preserve os textos aprovados e faça a navegação conduzir as transições.
```

```text
Use $motion-production para melhorar este motion existente.
Observe o resultado, identifique os problemas de ritmo e continuidade
e altere somente as propriedades necessárias.
```

## Instalação

No Codex, peça ao `$skill-installer` para instalar:

```text
https://github.com/renanmulinarixz/motion-production/tree/main/skills/motion-production
```

A skill também pode ser copiada integralmente para o diretório de skills reconhecido pelo agente. O repositório contém `plugin.json` e a estrutura `skills/motion-production/SKILL.md`; a distribuição no GitHub não implica publicação em um diretório oficial de plugins.

## Repertório incluído

- Vinte receitas de efeitos e uma análise por fases de oito referências de logos e elementos.
- Catálogo offline com oito folhas de contato e 2.102 frames consultáveis, com PTS, origem e limites da análise.
- Modelo de continuidade de 20 s/600 frames, com vídeo próprio e fonte Canvas editável.
- Referências de outros nichos, com distinção entre frame observado, processo documentado e análise automática.
- Contrato de produção neutro, três briefings de exemplo, verificador de contratos e diagnóstico local de capacidades.
- Renderizadores locais Chromium/FFmpeg e Canvas/Skia para fontes compatíveis.

Na pasta da skill, execute `python scripts/prepare_reference_frames.py` e abra `assets/pinterest-logos/index.html`. Para materializar os frames do modelo próprio, use `python scripts/prepare_reference_frames.py --source model` com FFmpeg disponível.

Os scripts de renderização exportam vídeo sem áudio. A produção de uma peça narrada inclui síntese ou gravação, sincronização e mixagem conforme o projeto. Os recursos locais têm dependências explícitas; a skill não instala nem autentica editores por conta própria.

## Escopos independentes

`motion-production` cuida da criação de motion e da adaptação ao ambiente. O repertório foi desenvolvido inicialmente em trabalhos BeSafe; esses trabalhos agora são [exemplos de projeto](skills/motion-production/references/project-examples.md). Sua paleta, tema, duração e voz não são padrões universais.

A skill [higgsfield-media-production](https://github.com/renanmulinarixz/higgsfield-media-production) cuida do uso da plataforma Higgsfield, incluindo seleção de modelos, benefícios, custos, execução e recuperação de gerações. Ela pode colaborar com um projeto de motion quando essa rota for escolhida.

## Verificação e direitos

Leia [validação e limites](skills/motion-production/references/validation.md) para o alcance dos testes e inspeções. Disponibilizar todos os frames não significa que cada frame tenha recebido análise visual individual.

Código e textos próprios sob MIT. Imagens externas e marcas mantêm os direitos de seus titulares, identificados nos registros de origem e no [aviso do acervo](skills/motion-production/assets/pinterest-logos/NOTICE.md). Use mecanismos como referência e ativos próprios ou autorizados na produção.
