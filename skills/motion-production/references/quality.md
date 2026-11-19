# Revisão e aceitação

## Conferir a entrega pelo seu objetivo

No vídeo inteiro, a sequência precisa produzir o efeito definido no brief. Em tamanho real e reduzido, o foco, o conteúdo e o resultado final devem continuar identificáveis. Nas fronteiras de movimento, verificar trajetórias, contato, recorte, deformação e acomodação.

| Tipo de peça | Conferência prioritária |
| --- | --- |
| Logo/identidade | Silhueta autorizada, instante de reconhecimento, proporção final e emenda quando houver loop |
| Tipografia/editorial | Texto exato, hierarquia, ritmo de entrada e tempo de leitura |
| Produto | Continuidade de geometria, detalhes importantes, escala e materialidade |
| Interface | Fidelidade do estado, alvo transformado, ação antes da resposta e legibilidade |
| Dados | Valores, unidades, escala, correspondência entre entidades e conclusão comunicada |
| Narrativa/música | Relação entre ações, tempo, som e progressão expressiva pretendida |

## Corrigir antes de entregar

Texto crítico errado, cortado ou ilegível; logo deformado no momento de reconhecimento; dado com sentido alterado; objeto que salta involuntariamente; cursor sem alvo; ausência inesperada de frames, fontes, assets ou áudio; duração/formato incompatíveis com o pedido; exportação que difere da prévia em conteúdo relevante.

Inspecionar o arquivo final, não apenas a timeline ou o HTML. Com fala, conferir pronúncia, cortes, legendas e sincronismo. Sem fala, conferir a linguagem sonora ou a versão muda conforme o briefing. Controle de reprodução e etiquetas de produção ficam fora da imagem final, salvo solicitação explícita.

## Verificar a mídia

Usar as ferramentas disponíveis para conferir codec, dimensões, duração, fps, contagem e faixas de áudio. Decodificar o arquivo inteiro quando possível. O teste estrutural não substitui inspeção visual nem demonstra compreensão pelo público.

Na rota local:

```text
ffprobe -v error -show_streams -show_format -of json video.mp4
ffmpeg -v error -i video.mp4 -f null -
ffmpeg -i video.mp4 -fps_mode passthrough -start_number 0 frames/frame-%06d.png
```

Em loop, comparar posição, forma, cor e direção na emenda. Em revisão, comparar antes/depois e os estados próximos à edição. Para fontes VFR, registrar os PTS originais em vez de assumir índice/fps.

Entregar o arquivo realmente produzido, fonte editável oferecida pela rota e limites ainda relevantes. Registrar separadamente o que foi testado, observado ou permaneceu sem execução.
