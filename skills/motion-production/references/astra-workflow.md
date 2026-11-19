# Processo de criação para Astra

Ler ao transformar um pedido em produção ou ao revisar um motion existente. Adaptar a profundidade à entrega: uma microanimação exige menos preparação que um filme de produto.

## Da intenção à linguagem

Descrever o que a pessoa deve perceber, sentir ou fazer ao final. Identificar público, contexto de exibição, marca, duração, proporção, som e editabilidade solicitada. Usar o material existente para resolver lacunas; perguntar somente quando a resposta mudar a próxima decisão dependente.

Escolher uma ideia visual que possa evoluir durante a peça. Exemplos: um traço constrói uma assinatura; módulos representam um sistema; um produto permanece enquanto suas características aparecem; um dado muda de escala sem perder a relação com a origem. Escrever essa ideia antes de escolher efeitos.

Definir contraste, escala, formas, tipografia, materiais, movimento e som em função dessa ideia. Uma marca editorial pode pedir pausas e recortes; uma peça musical pode seguir pulsação e repetição; uma demonstração de interface pede estabilidade na leitura. Usar a referência como mecanismo, sem impor sua paleta ou gênero ao projeto.

## Da referência ao movimento

Selecionar poucos trechos pertinentes. Registrar o frame inicial, o estado de maior transformação, o destino, a trajetória e o momento de repouso. Distinguir o que se vê da implementação proposta. Não deduzir plugin, software ou curva exata apenas pela aparência.

Para cada passagem, responder:

- Qual entidade ou relação conecta os dois estados?
- Onde o olhar deve estar antes, durante e depois da transformação?
- O movimento continua, muda de função ou termina em uma pausa?
- A forma final precisa estar legível em qual instante?

Nem toda transição exige morph. Reorganização, corte na ação, match cut, máscara, aproximação e corte simples têm funções distintas. Em uma narrativa com mudança real de tempo ou assunto, um corte pode ser a decisão adequada.

## Do storyboard à implementação

Preparar os estados que resolvem as maiores incertezas: composição inicial, transformação difícil e resultado. Confirmar a leitura na proporção de entrega. Fazer um animatic com formas simples para validar ritmo, causa e efeito, continuidade e duração antes de materiais complexos.

Escolher a rota com [adapters.md](adapters.md). A escolha considera controle necessário, editabilidade, acesso real, custo autorizado e capacidade de exportação. Em trabalho híbrido, declarar qual ferramenta gera o asset, qual anima e qual compõe texto e som.

Manter conteúdo, estado e apresentação separados. Dar IDs a entidades persistentes. Em código, calcular a apresentação por tempo absoluto; em editores, usar camadas e relações equivalentes. Para uma reprodução ou revisão pontual, o mesmo instante deve reconstruir o mesmo estado.

Implementar primeiro a passagem que ameaça o conceito. Quando ela funcionar, expandir o sistema de movimento ao restante da peça. Ajustar antecipação, percurso e acomodação à massa e ao estilo; não aplicar o mesmo quique a todo objeto.

## Da primeira versão à versão entregue

Rever em três escalas: a narrativa no vídeo inteiro; a composição no tamanho real e reduzido; o movimento nas fronteiras e instantes de deformação. Quando som for parte da linguagem, conferir a sincronização com os eventos visuais.

Traduzir o problema observado em uma correção localizada:

| Observação | Investigar e corrigir |
| --- | --- |
| A marca fica difícil de reconhecer | Silhueta, tempo de resolução, distorção e contraste antes de adicionar efeitos |
| A peça parece uma sequência de slides | Entidade compartilhada, mudança de enquadramento e ligação entre estados |
| Tudo compete pelo olhar | Hierarquia e simultaneidade de câmera, texto, gesto e fundo |
| O movimento parece sem peso | Relação entre distância, duração, aceleração e acomodação |
| O texto aparece enquanto ainda não pode ser lido | Instante de estabilização, escala e pausa disponível |
| Uma alteração desorganiza o restante | Propriedade editada, dependências e invariantes aprovadas |
| O export difere da prévia | Fontes, assets, tempo, renderizador, áudio e formato final |

Preservar o que já funciona. Não regenerar toda a peça para corrigir um pequeno alinhamento se a ferramenta permitir edição localizada. Se duas tentativas repetirem a mesma falha, mudar a representação ou a ferramenta responsável pelo trecho, respeitando o pedido e a autorização existentes.

Encerrar com a mídia realmente exportada e a fonte oferecida pela rota usada. Registrar roteiro/contrato, assets selecionados e limites materiais para facilitar uma revisão futura. Não prometer aumento de retenção sem avaliação com o público.
