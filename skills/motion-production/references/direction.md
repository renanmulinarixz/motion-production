# Direção de motion

## Contrato do projeto

Definir finalidade — reconhecimento de marca, explicação, desejo, narrativa, demonstração ou leitura de dados — e como a composição e o movimento a tornam perceptível. Identificar público, contexto de exibição, formato, duração, fps, som, idioma, marca e editabilidade. Decisões explícitas do usuário e material aprovado orientam o trabalho.

O contrato adaptável pode registrar `project`, `objective`, `output`, `style`, `entities`, `beats`, `audio`, `invariants` e `evidence`. Cada beat informa o intervalo, a intenção, as entidades relevantes, o foco, a ação e a passagem. A especificação neutra acompanha código, camadas de editor, cena 3D ou instruções para outra ferramenta.

Não assumir 20 segundos, 30 fps, 16:9, voz, paleta ou tema. Esses valores pertencem a exemplos. Reenquadrar para a proporção de entrega; não recortar automaticamente uma composição horizontal para vertical.

## Linguagem visual

Escolher uma família coerente de formas, tipografia, materiais, luz e movimentos. Relacionar a escolha ao conceito. A energia de um evento musical, a pausa de uma identidade sóbria e a precisão de uma demonstração técnica pedem ritmos diferentes.

Definir o elemento principal e o que o entorno permite perceber. Em tipografia, considerar extensão do texto, hierarquia, contraste e tempo estável antes de decidir tamanho. Reduzir texto quando isso preservar o sentido e a leitura. Conferir a peça no dispositivo e no tamanho reais de exibição.

A paleta e as escalas do modelo incluído são exemplos. Um novo projeto define sua identidade. Espaço negativo, textura e profundidade podem participar da linguagem; não precisam preencher todo repouso.

## Continuidade e transformação

Uma entidade persistente pode mudar posição, escala, forma, enquadramento ou função. O espectador precisa reconhecer a relação entre os estados. Identidade visual repetida sem trajetória não basta para uma passagem que pretende mostrar deslocamento.

Escolher entre reorganização, aproximação, máscara, match cut, corte na ação, morph e corte simples pela relação narrativa. Transformações incompatíveis de topologia podem usar máscaras ou estados intermediários. Não prometer interpolação limpa entre quaisquer dois caminhos.

Movimento envolve preparação, deslocamento e acomodação quando o estilo e a ação pedem essas fases. Ajustar duração à distância e à massa percebida. Trajetórias que continuam através de um beat não devem parar e reiniciar por uma divisão do roteiro.

## Foco, tempo e som

Organizar a atenção: uma ação pode conduzir outras, mas elas precisam de hierarquia. Câmera, tipografia, objeto e fundo não devem exigir leitura simultânea incompatível com o conteúdo. Em peças densas, planejar a ordem do olhar.

Texto, logo e dados essenciais chegam a um estado legível dentro do tempo aprovado. Definir o primeiro instante de reconhecimento e o repouso necessário. Não acelerar toda a voz ou o filme para compensar um roteiro que não cabe.

Quando som fizer parte do conceito, escolher sua função: fala, pulsação, textura ou evento causal. Conferir sincronismo e mixagem no arquivo final. Legendas, voz e acessibilidade seguem a necessidade e o briefing do projeto; a voz Francisca é uma decisão das aulas BeSafe descrita nos exemplos.

## Implementação consistente

- Separar texto/dados, estado narrativo e apresentação visual.
- Dar IDs às entidades que precisam persistir; conservar contagem e significado quando fizerem parte da ideia.
- Em código, reconstruir o estado por tempo absoluto, com aleatoriedade controlada e assets carregados.
- Em editores, usar relações de camadas, hierarquia e keyframes que preservem a mesma intenção.
- Compartilhar transformações entre alvo, cursor, máscara, destaque e legenda ligada ao objeto.
- Definir quais propriedades podem mudar em uma revisão e o que precisa permanecer.
- Guardar a especificação e os arquivos de passagem em projetos com várias ferramentas.

Na versão offline, usar assets e fontes locais. O contrato temporal do exemplo Canvas usa segundos, índices 0…599 para 20 s a 30 fps e `t = índice / fps`. Outros formatos usam seus próprios valores. Fontes VFR exigem PTS reais na catalogação.
