# Validação e histórico de evidências

Os registros de 17 e 19/11 abaixo documentam a origem do acervo e os testes daquela execução. A seção final distingue a distribuição geral `motion-production` e seus testes próprios.

- Entrada e frontmatter passaram no validador de skills.
- Modelo próprio: 600 imagens JPEG decodificadas do MP4 final, 1440 × 810, timestamps de 0 a 19,966667 s; integridade de todas as imagens conferida.
- 9 imagens externas locais verificadas; 3 registros Higgsfield mantidos sem imagem porque o download retornou HTTP 403.
- Galeria: navegação inicial/final, limites, salto para clique e setas passaram em teste de lógica JavaScript. Layout do HTML não foi testado em navegador local nesta etapa; Chromium falhou por restrição de socket do ambiente.
- Renderizador Chromium: tentativa real, lançamento bloqueado pelo ambiente. Não declarar exportação Chromium validada nesta sessão.
- Renderizador Canvas/Skia: execução completa de 20 s, 600 quadros, 30 fps, H.264, 1440 × 810, sem áudio e sem chamadas de rede. FFprobe e decodificação integral passaram.
- Inspeção visual de abertura, concentração, clique, redistribuição e conclusão detectou inicialmente fallback de fonte e interpretação incorreta do peso 750. Correção: registrar fontes locais compatíveis com Arial e arredondar pesos numéricos para centenas. Nova exportação e inspeção passaram nos quadros selecionados. Não houve inspeção manual de cada um dos 600 quadros do novo render.
- A referência visual continua sendo o MP4 original e seus 600 quadros. O adaptador Skia pode diferir em antialiasing, sombras e fontes. Não prometer equivalência pixel a pixel.
- Higgsfield: documentação pública e rotas observadas; geração e edição nativa não executadas. Quatro YouTube: análise automática, sem arquivos para extração.

Repetir apenas os testes afetados por futuras alterações. Exportação estruturalmente válida não substitui revisão de conteúdo, leitura e continuidade.

## Uso independente
Uma execução independente preparou um contrato Gmail de 20 s a partir da skill: cinco beats contínuos, textos exatos, IDs persistentes, clique causal, domínio fictício, ancoragem transformada e ressalva de segurança. O JSON e as pausas foram conferidos. O agente consultou três frames pelo manifesto; iniciou antes de a galeria estar pronta. A galeria foi concluída e validada depois. Esse teste valida a preparação do contrato, não uma aula Gmail renderizada.
# Distribuição de referências de logos

O catálogo adicional foi elaborado em 19/11/2026 com oito vídeos obtidos de posts públicos do Pinterest. Os 2.102 frames são distribuídos em arquivos frames.zip por fonte. Executar scripts/prepare_reference_frames.py para materializá-los. O manifesto contém PTS extraídos por FFprobe e rótulos editoriais por intervalo. A inspeção visual abrange folhas de contato amostradas e estados de fronteira. Consultar references/logo-elements.md para o alcance da análise e a autoria pendente. Na distribuição compacta, os 600 JPEGs do modelo próprio podem ser materializados a partir de assets/model.mp4 com o mesmo script e a opção --source model.

## Retomada e conferência do pacote — 19/11/2026

- As duas skills passaram no validador de frontmatter, nomes e scaffolding.
- Metadados de motion convertidos de CP1252 para UTF-8; os 28 arquivos de texto da skill passaram na leitura UTF-8. Galeria e extração passaram a gravar explicitamente UTF-8, inclusive no Windows.
- Oito ZIPs passaram no CRC e na correspondência exata entre seus membros, manifesto e arquivos materializados: 2.102 frames. Índices, PTS crescentes, fases e sincronização com catalog.js conferidos.
- As 2.719 imagens locais (2.102 frames Pinterest, 600 do modelo, oito folhas de contato e nove stills externos) foram abertas e decodificadas por Windows System.Drawing. Dimensões dos frames e hash SHA-256 do MP4 próprio conferidos.
- As oito folhas de contato foram novamente inspecionadas visualmente. Isso não constitui inspeção individual de todos os 2.102 frames.
- Catálogo de logos aberto em Chrome headless, captura de tela inspecionada. Testados início, meio e fim de cada slider: 24 verificações de atualização do caminho da imagem e do rótulo, sem erros. A decodificação integral dos arquivos foi verificada separadamente.
- Links Markdown locais, metadados de interface e sintaxe Python/Node conferidos. Galeria do modelo regenerada com 600 entradas e nove imagens externas.
- A voz Francisca Neural aprovada nas aulas foi registrada em direction.md. Não houve nova síntese, mixagem ou produção de aula nesta retomada.
- O ambiente local desta conferência tem Python, Node e Chrome, mas o diagnóstico da skill não encontrou FFmpeg, FFprobe, Playwright nem @napi-rs/canvas nas rotas disponíveis. Nenhum novo MP4 foi renderizado; os testes históricos de exportação acima não devem ser atribuídos a esta máquina.

## Distribuição geral Motion Production — 19/11/2026

- A skill foi separada em pacote próprio com nome `motion-production`, entrada geral e metadados coerentes. BeSafe passou a ser um caso de origem em project-examples.md. Público, marca, tema, duração, proporção, som e ferramenta são escolhas de cada projeto.
- O processo do Astra cobre direção visual, análise de referências, estados e passagens, animatic, escolha por capacidades, implementação e revisão localizada. Os adaptadores distinguem execução local, editores, 3D, geração e fluxos híbridos.
- Os 26 assets binários distribuídos foram preservados byte a byte em relação ao pacote de origem. Os 2.702 frames materializados também foram preservados para consulta local. A distribuição Git inclui os ZIPs e o MP4, com materialização reproduzível.
- Frontmatter, nome, descrição e metadados passaram no validador de skills. Os 34 arquivos de texto da skill foram lidos em UTF-8, sem caracteres de substituição; links Markdown locais conferidos.
- O acervo completo voltou a passar na verificação de arquivos: oito ZIPs/2.102 frames, manifesto, PTS crescentes, fases e catalog.js. As 2.719 imagens locais foram decodificadas via Windows System.Drawing. O catálogo no novo caminho passou nas 24 verificações de caminhos/rótulos em Chrome headless.
- Três contratos de gêneros diferentes passaram no novo check_brief.py: logo quadrado em loop, produto vertical com som e história de dados horizontal a 24 fps. Cinco casos inválidos foram recusados: ID duplicado, alvo desconhecido, beat fora da duração, ciclo de parentesco e pausa maior que o beat.
- Sintaxe Python e Node conferida. O diagnóstico local detectou corretamente Chrome e Edge além de Python/Node, sem declarar acesso a editores ou exportação disponível. Playwright, Canvas/Skia, FFmpeg e FFprobe continuam ausentes das rotas consultadas.
- Os contratos são exemplos de planejamento e os testes verificam as propriedades indicadas. Não representam três novos vídeos renderizados nem validação com espectadores.
