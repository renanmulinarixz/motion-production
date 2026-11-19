# Seleção de ferramentas e execução

Escolher a rota a partir do resultado solicitado e das capacidades confirmadas nesta sessão. Preservar a preferência explícita do usuário. A ausência de uma ferramenta muda a implementação possível, não transforma o briefing em um pedido de outra estética.

## Descobrir o ambiente

1. Conferir ferramentas conectadas e seus esquemas, acesso ao aplicativo/editor, arquivos existentes e restrições da execução.
2. Para uma rota local, executar `scripts/capabilities.py`. O diagnóstico procura executáveis e módulos sem iniciar geração nem instalar dependências.
3. Distinguir executável encontrado, editor acessível, recurso documentado, teste executado e exportação aprovada.
4. Relacionar o que precisa ser controlado: texto, camadas, geometria, personagem, câmera, som, formato e possibilidade de revisão.
5. Escolher a rota que atende esses requisitos com o acesso e o orçamento disponíveis. Documentar somente as limitações que afetam a entrega.

## Fluxo de produção
1. Ler o brief e escolher no máximo três referências úteis ao objetivo.
2. Detectar capacidades reais: arquivos, navegador, FFmpeg, renderizador, ferramentas conectadas, acesso ao editor e limites.
3. Criar roteiro com beats; atribuir IDs persistentes às entidades.
4. Preparar três quadros: abertura, transformação principal e conclusão.
5. Fazer um animatic com geometria simples; avaliar compreensão sem efeitos.
6. Aplicar tipografia, materiais, cursor, luz e transições.
7. Renderizar por tempo absoluto e inspecionar fronteiras de cada transição.
8. Ver o vídeo inteiro em velocidade normal e a versão reduzida.
9. Corrigir a causa do erro, renderizar a parte afetada e conferir o resultado final.
10. Entregar vídeo, fonte editável e evidências de verificação. Não chamar HTML animado de MP4.

Seleção:
- Texto exato, Gmail, chat, gráficos e demonstrações: rota local determinística.
- Composição Adobe editável solicitada e conexão disponível: After Effects.
- Edição, mixagem, cortes e legendas: Premiere.
- Motion no navegador Higgsfield solicitado: verificar especificamente Vibe Motion; não substituí-lo silenciosamente por geração de vídeo comum.
- Higgsfield AI Motion Designer: rota separada, ligada ao editor Adobe.
- Cena cinematográfica ou textura orgânica: ferramenta generativa apenas para o trecho que precisa dela.
- 3D com câmera e luz editáveis: Blender quando disponível.
- Storyboard de produto: Figma quando disponível; confirmar como exportar a animação.
- React/Remotion: usar quando o projeto já o adota ou quando houver vantagem clara. O modelo principal não depende dele.

Falha de capacidade: registrar o bloqueio e avançar nas etapas independentes. Não instalar editores, alugar GPU, criar novas assinaturas ou consumir créditos apenas para “estudar” um recurso.



## Adaptações por ferramenta
| Rota | Unidade principal | Implementação sugerida | Verificação necessária |
| --- | --- | --- | --- |
| HTML/Canvas/SVG local | Estado por tempo absoluto | Interpolação, clipping, transforms e desenho vetorial | Mesmo t produz mesmo estado; fontes prontas |
| After Effects | Camadas, precomps e keyframes | Parenting, masks, track mattes e curvas de velocidade | Inspecionar composição e render; não rasterizar texto antes da hora |
| Premiere | Clips e sequência | Montagem, áudio, legendas, ajustes e gráficos disponíveis | Exportação, sincronismo e leitura; confirmar versão e recursos |
| Higgsfield Vibe Motion | Projeto conversacional | Brief por entidades, beats e alterações pequenas | Capacidade presente na UI e exportação real |
| Higgsfield AI Motion Designer | Projeto Adobe | Verificar conexão local; usar camadas e tempos editáveis | Chamada real ao editor; não substituir pelo sandbox de nuvem |
| Runway | Trecho generativo | Movimento de objeto/câmera em linguagem clara | Texto, logos e UI compostos separadamente quando exatidão for necessária |
| Figma | Componentes e estados | Planejar layout e correspondência de objetos | Exportação de motion não presumida; verificar ferramentas |
| Blender | Objetos, câmera e materiais | Formas, iluminação e animação controladas | Câmera, duração, samples e render |
| Remotion | Frame e componentes React | Derivar animação do frame atual e props | Dependências existentes; render determinístico |
| Astra/Codex | Planejamento e código | Roteirizar, implementar, avaliar e adaptar | Não tratar o modelo como um codec ou aplicativo de renderização |

After Effects: a documentação consultada descreve Graph Editor e controles da velocidade entre keyframes. Use curvas com intenção; Easy Ease não resolve por si só toda a direção de movimento.
Fonte: https://helpx.adobe.com/after-effects/using/speed.html

Runway/Figma/Blender/Remotion: esta tabela define papéis de produção, não certifica integração instalada nem suporte a toda versão. Descobrir o esquema e a documentação atual ao executar.


### Exportação local sem navegador
O script render_canvas.cjs é uma alternativa explícita para o template Canvas confiável. Usa @napi-rs/canvas e FFmpeg locais. Não interpreta CSS/DOM/SVG nem carrega fontes web. Validar métricas e substituição de fontes; não prometer equivalência pixel a pixel com Chromium. O modo não chama APIs nem provedores. Para HTML desconhecido, não usar essa execução; node:vm não constitui isolamento de segurança.

### Requisitos e passagem entre ferramentas

- `render.cjs`: Node, Playwright, Chromium compatível e FFmpeg. A variável `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH` pode indicar um navegador local. A detecção não prova que ele inicia no ambiente.
- `render_canvas.cjs`: Node, `@napi-rs/canvas`, FFmpeg e fontes/fontconfig compatíveis com o adaptador atual. A detecção do módulo isolado não confirma exportação.
- Os dois scripts fornecem vídeo sem áudio. Definir a ferramenta de som/montagem quando a peça o exigir.
- Em fluxo híbrido, registrar formato, dimensões, fps, alpha, espaço de cor e duração necessários na passagem; conferir quais opções a ferramenta realmente exporta.
- Com texto ou logo exatos, escolher uma representação que permita preservar e revisar sua forma. Tratar o resultado gerativo como material sujeito a composição e revisão.

Para Higgsfield, este adaptador define apenas sua função no motion. A skill independente `higgsfield-media-production` cuida dos modelos, benefícios, custos e recuperação de gerações.
