# Modelo conceitual da interação entre Tessitura e Narrador

> Status: compreensão conceitual atual, ainda sem especificação técnica completa.

Este documento descreve como Jogador, Tessitura e Narrador deverão colaborar
para conduzir uma campanha. Ele ocupa uma posição intermediária entre o
[guia geral do projeto](project-guide.md) e os documentos especializados dos
motores, como o [motor narrativo](domain/narrative-engine.md). A
[linguagem ubíqua](domain/ubiquitous-language.md) permanece transversal a
todos eles.

Os nomes e as estruturas apresentados aqui registram o modelo atualmente
compreendido. Eles não determinam antecipadamente classes, schemas, formatos
de persistência, APIs ou prompts.

## Premissa central

Tessitura deverá administrar o estado estruturado e resolver tudo que puder
ser expresso como regra estável. O Narrador deverá transformar resultados em
prosa e participar das decisões que exijam interpretação semântica, criação ou
escolha entre alternativas narrativamente válidas.

O ponto focal dessa colaboração é a Interação. Para cada Interação, o Narrador
deverá receber um recorte do mundo preparado especificamente para aquilo que
precisa narrar. Esse recorte é denominado provisoriamente `NarrativeFrame`.

O `NarrativeFrame` não representa o mundo inteiro, o histórico completo nem a
fonte oficial da verdade. Ele é uma projeção contextual do estado que reúne a
situação atual, a transição focal, a continuidade necessária e os limites de
interpretação do Narrador.

## Qualidades dos dados apresentados ao Narrador

Os dados de uma Interação deverão observar as seguintes qualidades:

- **minimamente suficientes:** deverão formar o menor conjunto capaz de
  sustentar corretamente a próxima atividade do Narrador;
- **relevantes:** cada informação deverá possuir uma razão concreta para estar
  no contexto atual;
- **consistentes:** não deverão contradizer o Cânone da História, o Estado do
  Mundo ou compromissos narrativos anteriores;
- **temporalmente situados:** deverão indicar o momento ou intervalo em que
  são válidos e distinguir informação vigente de informação superada;
- **epistemicamente qualificados:** deverão distinguir fatos objetivos,
  percepções, conhecimentos, crenças, rumores, mentiras e hipóteses;
- **rastreáveis:** quando necessário, deverão permitir identificar sua origem
  e a autoridade responsável por estabelecê-los;
- **não ambíguos:** identidades e relações deverão permanecer distinguíveis,
  mesmo quando a prosa empregar referências informais;
- **perspectivados:** deverão respeitar aquilo que cada observador pode
  perceber ou conhecer;
- **causalmente informativos:** deverão incluir os antecedentes necessários
  para compreender por que o estado atual existe;
- **explícitos sobre lacunas:** ausência de informação não deverá ser
  confundida com negação ou inexistência;
- **orientados à decisão atual:** deverão deixar claro o que precisa ser
  narrado, calculado, interpretado ou decidido.

Minimalismo e suficiência não são objetivos opostos. O objetivo não é fornecer
o máximo de informação possível, mas alcançar **suficiência mínima
contextual**.

## Responsabilidades na Interação

As responsabilidades atualmente compreendidas são:

- o **Jogador** determina suas falas, escolhas e intenções;
- **Tessitura** mantém as fontes de verdade, aplica regras, calcula resultados,
  identifica lacunas interpretativas, valida solicitações e decisões e controla
  alterações do mundo;
- o **Narrador** interpreta as Declarações do Jogador, converte o significado
  compreendido em solicitações estruturadas ao Tessitura, resolve as questões
  interpretativas que lhe forem delegadas e apresenta ao Jogador uma Resposta
  do Narrador em prosa;
- o **NarrativeFrame** transporta para o Narrador a projeção relevante e
  estruturada de uma Interação.

O Narrador participa da criação da realidade do jogo, mas sua participação não
deverá modificar implicitamente o Cânone da História ou o Estado do Mundo.
Decisões capazes de produzir consequências futuras deverão ser identificadas,
validadas e aplicadas pelo Tessitura.

## Ciclo conceitual da Interação

O ciclo atualmente compreendido é:

```text
Estado do Mundo N
        ↓
seleção e projeção do contexto relevante
        ↓
NarrativeFrame N
        ↓
Narrador produz a Resposta do Narrador
        ↓
Jogador produz uma Declaração do Jogador
        ↓
Narrador interpreta a Declaração do Jogador
        ↓
Narrador esclarece ambiguidades materiais com o Jogador, quando necessário
        ↓
Narrador formula uma solicitação estruturada e aciona o Tessitura
        ↓
Tessitura valida a solicitação e identifica as operações e regras aplicáveis
        ↓
resolução determinística possível
        ↓
Questões Narrativas ainda necessárias
        ↓
Narrador fornece decisões estruturadas e justificadas
        ↓
Tessitura valida e aplica as consequências permitidas
        ↓
Estado do Mundo N+1
        ↓
seleção e projeção do novo contexto relevante
        ↓
NarrativeFrame N+1
```

Uma resposta narrativa poderá criar condições para novos cálculos, e um novo
cálculo poderá revelar outra lacuna interpretativa. A resolução das Questões
Narrativas poderá, portanto, exigir mais de uma alternância entre Tessitura e
Narrador antes que o estado necessário ao próximo `NarrativeFrame` esteja
consolidado.

O Narrador realiza a interpretação semântica porque é ele quem recebe a
linguagem livre do Jogador e aciona o Tessitura. Essa interpretação não lhe dá
autoridade para redefinir a vontade do Jogador. Quando uma ambiguidade puder
alterar materialmente a ação, o alvo, as condições ou as consequências
pretendidas, o Narrador deverá pedir esclarecimento ao Jogador antes de formar
a solicitação estruturada.

O Tessitura não interpreta diretamente a linguagem livre nesse ciclo. Ele
recebe a solicitação estruturada, verifica sua validade diante do estado atual
e identifica as operações e regras aplicáveis. A forma concreta dessa
solicitação e o mecanismo usado pelo Narrador para produzi-la permanecem em
investigação.

## Estado do Mundo e NarrativeFrame

As interpretações anteriores do Narrador não deverão ser acumuladas como
transcrições dentro de cada novo `NarrativeFrame`. Quando validadas e
aplicadas, suas consequências passam a integrar as fontes de verdade
apropriadas. O frame seguinte recupera somente aquilo que continuar relevante.

```text
Decisão do Narrador
        ↓
validação e aplicação pelo Tessitura
        ↓
compromisso registrado no mundo
        ↓
seleção conforme o foco da próxima Interação
        ↓
NarrativeFrame
```

Essa separação permite que o mundo preserve mais informação do que o Narrador
recebe em uma Interação. Também impede que o frame se torne um segundo Estado
do Mundo ou um histórico narrativo cada vez maior.

## Estrutura conceitual do NarrativeFrame

O `NarrativeFrame` deverá responder principalmente:

- **o quê:** qual acontecimento, ação ou pergunta constitui o foco atual;
- **onde:** qual é o espaço relevante e como seus elementos se relacionam;
- **quando:** qual é o momento ficcional e quais durações ou prazos importam;
- **quem:** quais participantes são relevantes e em que condições estão;
- **como:** qual é o estado atual e qual transição o produziu;
- **por quê:** quais causas, objetivos, motivações e riscos são pertinentes;
- **sob quais limites:** o que está estabelecido, o que pode ser interpretado
  e o que não pode ser presumido.

Uma possível organização sem compromisso com formato de implementação é:

```yaml
narrative_frame:
  reference:
    interaction: ...
    sequence: ...
    world_time: ...
    schema_version: ...

  focus:
    trigger: ...
    narrative_question: ...
    expected_output: ...
    stakes: ...

  situation:
    place:
      reference: ...
      relevant_features: ...
      spatial_relations: ...

    time:
      current_moment: ...
      elapsed_time: ...
      active_deadlines: ...

    participants:
      - reference: ...
        role_in_interaction: ...
        current_state: ...
        declared_intention: ...
        relevant_motivations: ...
        knowledge: ...
        relationships: ...

    relevant_elements: ...
    established_state: ...

  transition:
    initiating_action: ...
    target: ...
    deterministic_resolution: ...
    resulting_changes: ...
    immediate_consequences: ...

  continuity:
    relevant_antecedents: ...
    unresolved_threads: ...
    narrative_commitments: ...

  authority:
    fixed: ...
    interpretable: ...
    unknown: ...
    forbidden_to_assume: ...

  presentation:
    point_of_view: ...
    intended_audience: ...
    tone: ...
    detail_level: ...
```

Os campos ilustram dimensões já discutidas; não estabelecem que todas estarão
presentes em todo frame. O formato concreto deverá manter a possibilidade de
omitir dimensões irrelevantes sem perder a capacidade de distinguir ausência,
negação e desconhecimento.

### Foco

O foco informa o que o Narrador deve realizar naquela chamada. Sem ele, mesmo
um contexto correto pode produzir uma resposta dispersiva. O Narrador precisa
saber se deverá apresentar uma consequência, interpretar uma reação, compor
uma cena ou fornecer uma decisão estruturada.

### Situação e transição

A situação descreve como o mundo se encontra agora. A transição registra o que
está acontecendo ou o que acabou de ser resolvido. O Narrador não deverá
reconstruir o estado atual percorrendo todo o histórico, mas deverá receber a
causalidade necessária para preservar a continuidade.

### Autoridade

O frame deverá diferenciar:

- dados **fixos**, que o Narrador não pode contradizer;
- espaços **interpretáveis**, nos quais existem várias soluções válidas;
- aspectos **desconhecidos**, cuja ausência deve ser preservada;
- suposições **proibidas**, que romperiam o estado, a perspectiva ou a agência
  do Jogador.

Essa divisão protege tanto os resultados determinísticos contra alterações
arbitrárias quanto a liberdade criativa do Narrador contra uma mecanização
indevida.

### Qualificação das afirmações

Origem, validade, perspectiva e autoridade frequentemente pertencem a uma
informação específica, não ao frame inteiro. Uma crença de um personagem e um
fato objetivo podem empregar frases semelhantes sem representar a mesma coisa.

Conceitualmente, uma informação sensível a essas diferenças poderá precisar
de qualificações como:

```yaml
statement:
  content: "O guarda acredita que Lina é uma contrabandista"
  epistemic_status: belief
  holder: guard
  source: previous_interaction
  validity: current
  visibility: narrator_only
  authority: fixed
```

Isso não estabelece uma classe universal de afirmação nem uma estrutura
genérica de chave e valor. A representação concreta deverá emergir quando os
primeiros dados reais exigirem essas distinções.

## Questões Narrativas e respostas

A [Questão Narrativa](domain/narrative-engine.md#questões-narrativas) é a
unidade acordada para solicitar uma decisão interpretativa ou criativa ao
Narrador. Ela não representa toda comunicação entre Narrador e Tessitura.

No ciclo da Interação, Tessitura deverá criar uma questão quando a continuação
depender de uma decisão que não possa ser legitimamente deduzida por uma regra
estável. O Narrador fornece a decisão e sua Justificativa do Narrador; responder
à questão e aplicar suas consequências permanecem operações diferentes.

Para participar de uma transição reproduzível, a decisão deverá possuir uma
forma semanticamente estruturada. Duas respostas em prosa podem expressar a
mesma decisão, enquanto textos parecidos podem esconder decisões diferentes.
É o significado estruturado validado, e não a redação livre isolada, que deverá
alimentar a transição seguinte.

A questão também é estruturada e não precisa conter um enunciado em prosa. Seu
tipo concreto define qual decisão está pendente, quais dados se relacionam a
ela e qual resposta pode ser recebida. O contexto continua necessário para
fundamentar a decisão, mas não precisa repetir a operação em forma de pergunta.

Dentro do domínio, a classe concreta distingue os tipos de questão. Um contrato
externo que transporte diferentes tipos por um mesmo canal deverá serializar
essa distinção por meio de um discriminador como `kind`. O schema da ferramenta
ou operação define a resposta esperada. Assim, nem `kind` nem uma descrição do
schema precisam ser duplicados como campos nas entidades atuais.

`initial_context` permanece textual nos recortes implementados. Ele registra os
dados apresentados ao Narrador e não substitui o futuro recorte estruturado do
Cânone e do Estado do Mundo. A forma desse contexto deverá emergir quando essas
fontes existirem; não será antecipada como um objeto genérico neste momento.

Uma resposta narrativa também poderá criar a necessidade de outra questão. O
novo `NarrativeFrame` só deverá ser formado quando as lacunas necessárias ao
próximo ponto de interação estiverem suficientemente resolvidas.

## Reprodutibilidade

O processo completo não é determinístico, pois Jogador e Narrador realizam
escolhas. A transformação executada pelo Tessitura deverá ser reproduzível
depois que essas escolhas estiverem representadas como entradas explícitas.

Conceitualmente:

```text
novo_estado = transição(
    estado_anterior,
    solicitação_estruturada,
    resultados_mecânicos,
    respostas_narrativas,
    versão_das_regras,
    aleatoriedade_registrada,
)

novo_frame = projeção(
    novo_estado,
    foco_da_próxima_interação,
    perspectiva_aplicável,
)
```

Outro Narrador que forneça as mesmas decisões canônicas deverá conduzir o
Tessitura ao mesmo novo estado e ao mesmo frame lógico, desde que também sejam
iguais:

- o estado inicial;
- a solicitação estruturada produzida a partir da Declaração do Jogador;
- a versão das regras;
- os resultados aleatórios ou a semente utilizada;
- as fontes externas relevantes;
- o algoritmo e a versão da projeção.

Relógio implícito, aleatoriedade não registrada, interpretação oculta de texto
livre ou dependências externas mutáveis romperiam essa propriedade.

## Continuidade descritiva

Quando o Narrador participar da criação de uma pessoa, lugar ou objeto, deverá
fornecer um pequeno conjunto de detalhes estilísticos estruturados. Esses
traços descritivos acompanham o elemento criado e podem ser recuperados em
`NarrativeFrames` futuros quando forem relevantes.

Exemplos incluem:

- uma cicatriz que atravessa a sobrancelha de uma pessoa;
- uma voz baixa e pausada;
- a fachada de um lugar coberta por trepadeiras;
- inscrições no punho de uma espada.

Esses traços diferem de condições mutáveis e de efeitos de apresentação:

- uma cicatriz pode ser um traço relativamente estável da pessoa;
- roupas cobertas de lama representam seu estado atual;
- uma iluminação que faz o rosto parecer ameaçador pode pertencer somente à
  apresentação daquela cena.

O termo **traço descritivo** é usado aqui para evitar confusão com a Âncora
Narrativa, que já possui significado específico no motor narrativo. Sua adoção
como termo definitivo da linguagem ubíqua ainda não foi decidida.

A Resposta do Narrador deverá reutilizar os traços recebidos no frame em vez de
reinventar continuamente pessoas, lugares e objetos. Ainda não está decidido
se uma resposta ao Jogador poderá estabelecer novos fatos persistentes fora de
um fluxo explícito de criação ou decisão narrativa.

## Mapa atual de responsabilidades especializadas

Um mundo completo exigirá vários conjuntos de regras, mas isso não autoriza a
criação antecipada de uma engine, classe ou módulo para cada assunto. Uma
responsabilidade merece tornar-se uma engine quando possuir regras,
invariantes, entradas e resultados próprios e quando essa separação for
confirmada pelo comportamento real do sistema.

As áreas abaixo formam o mapa conceitual atualmente discutido.

### Narrative Engine

Administra o compromisso narrativo progressivo, incluindo Intenções,
Preparações, Situações e decisões discricionárias governadas por Questões
Narrativas. Ela não deverá absorver regras mecânicas apenas porque seus
resultados serão narrados.

### Rules Resolution Engine

Aplica as regras do sistema de RPG às ações e ao estado: testes, modificadores,
rolagens, recursos, condições, dano, recuperação, ações, reações, habilidades e
magias. Combate permanece, por enquanto, uma possível especialização dessa
responsabilidade, não uma engine necessariamente independente.

### Temporal Engine

Administra tempo ficcional, duração, ordem, simultaneidade, prazos, agendas,
efeitos temporários, eventos programados e avanço de tempo. O tempo ficcional
deverá permanecer distinto do relógio real usado para auditoria.

### Spatial Engine

Administra mapas e as relações espaciais do mundo, incluindo continência,
adjacência, distância, alcance, rotas, acessibilidade, ocupação, cobertura,
linha de visão e movimento possível.

Também é responsável por distribuir e localizar pessoas, objetos, itens e
prêmios nos lugares do mundo e por permitir que essa distribuição seja
consultada. Essa responsabilidade espacial estabelece onde algo está, como
pode ser alcançado e, quando aplicável, se pode ser encontrado. As propriedades
mecânicas de um item, as regras de posse ou o significado narrativo de um
prêmio podem pertencer a outras responsabilidades.

### World Evolution Engine

Produz transições válidas sobre o Estado do Mundo, aplica consequências,
propaga efeitos derivados, processa acontecimentos disparados e atualiza áreas
que evoluíram fora da cena imediata. O Cânone da História e o Estado do Mundo
são fontes de verdade; não precisam, por isso, ser engines.

### Epistemic Engine

Administra as diferenças entre verdade, percepção, conhecimento, crença,
suspeita, rumor, mentira e informação oculta. Determina qual versão do mundo
pode ser apresentada a cada observador sem transformar percepção em fato ou
revelar conhecimento indevido.

### Context Projection Engine

Seleciona e organiza o contexto necessário ao Narrador, produzindo um
`NarrativeFrame` compacto, perspectivado, rastreável e reproduzível. Essa
responsabilidade não altera o mundo e poderá revelar-se um serviço de aplicação
em vez de uma engine de domínio.

### Outras pressões identificadas

Um mundo mais completo poderá revelar responsabilidades coerentes relacionadas
a:

- atores, rotinas, necessidades, prioridades e ordens;
- relações, reputação, hierarquias, facções e influência;
- encontros condicionados por lugar, tempo, ruído, rastros e disponibilidade;
- ambiente, clima, iluminação, terreno, ecologia e populações;
- economia, propriedade, inventário, produção, consumo e recursos;
- viagem, exploração, navegação, suprimentos e fadiga;
- progressão, treinamento, marcos e aquisição de capacidades.

Essas responsabilidades não estão estabelecidas como engines independentes.
Algumas poderão permanecer como partes das engines anteriores ou como fluxos
que coordenam várias delas.

## Contribuição para o NarrativeFrame

O frame poderá reunir respostas de autoridades especializadas sem transformar
nenhuma delas em dona de toda a Interação:

| Dimensão | Fonte conceitual provável |
| --- | --- |
| Local, mapa e distribuição espacial | Spatial Engine |
| Momento, duração e prazos | Temporal Engine |
| Resultado mecânico | Rules Resolution Engine |
| Consequências já aplicadas | World Evolution Engine |
| Conhecimento e perspectiva | Epistemic Engine |
| Importância e compromisso narrativo | Narrative Engine |
| Seleção do que será apresentado | Context Projection Engine |

O coordenador da Interação deverá combinar essas contribuições sem exigir que
uma engine conheça detalhes internos das demais. A localização de uma espada,
por exemplo, pode pertencer à responsabilidade espacial; seus efeitos
mecânicos, às regras; sua importância para uma Intenção, ao motor narrativo; e
sua visibilidade no frame, à projeção contextual.

## Resolução variável do mundo

Completude não significa simular todos os elementos com a mesma resolução o
tempo inteiro. O mundo poderá manter:

- alta resolução ao redor da Interação atual;
- evolução resumida em áreas que continuam ativas em segundo plano;
- estado dormente onde nenhum acontecimento exige cálculo.

Ao se tornar relevante, uma área deverá poder ser atualizada coerentemente a
partir do estado e dos acontecimentos aplicáveis. Essa diferença de resolução
permite preservar um mundo amplo sem exigir cálculo contínuo de cada pessoa,
objeto e lugar.

## Decisões ainda abertas

Este modelo ainda não determina:

- a representação concreta do `NarrativeFrame`;
- quais de suas dimensões serão obrigatórias;
- como o Narrador converterá a Declaração do Jogador em uma solicitação
  estruturada ao Tessitura;
- como Questões Narrativas encadeadas serão coordenadas;
- como respostas narrativas serão representadas de maneira canônica;
- como traços descritivos serão armazenados e selecionados;
- se a Resposta do Narrador poderá introduzir novos compromissos persistentes;
- como o contexto relevante será selecionado e aprofundado sob demanda;
- como aleatoriedade, versões e fontes externas serão registradas;
- quais responsabilidades especializadas merecerão engines próprias.

Essas lacunas são limites explícitos da compreensão atual. Elas deverão ser
resolvidas uma unidade conceitual por vez, quando o software produzir pressão
concreta para cada decisão.
