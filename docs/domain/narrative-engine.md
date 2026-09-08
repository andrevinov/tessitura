# Motor narrativo

## Questões Narrativas

A Questão Narrativa é a unidade acordada para solicitar a participação interpretativa ou criativa do Narrador. O Tessitura apresenta um enunciado e contexto; o Narrador responde e justifica sua decisão na questão. Responder e aplicar as consequências são operações distintas. Esse modelo orienta a evolução do motor, mas ainda não substitui todos os fluxos existentes.

Uma Questão Narrativa não representa toda interação entre o Narrador e o Tessitura. Consultar contexto, solicitar detalhes adicionais, executar regras determinísticas, receber resultados mecânicos e compor a Resposta do Narrador ao Jogador podem ocorrer sem criar uma questão. A questão aparece quando o Tessitura precisa governar e auditar uma interpretação, criação ou escolha entre alternativas narrativamente válidas. Uma Resposta do Narrador pode apoiar-se em várias decisões anteriores sem ser, ela própria, uma Questão Narrativa.

Essa fronteira preserva responsabilidades diferentes. O Tessitura formula a questão e seleciona o contexto pertinente; o Narrador fornece a decisão e sua justificativa; uma operação posterior valida e aplica as consequências permitidas. Cânone da História e Estado do Mundo podem fornecer contexto e receber consequências controladas, mas não são modificados diretamente pela resposta à questão.

O primeiro recorte implementado é `BinaryNarrativeQuestion`, uma entidade de domínio com identidade própria (`id`), referência à Intenção relacionada à decisão desse recorte (`intention_id`), enunciado (`prompt`) e contexto inicial (`initial_context`). A referência à Intenção não foi estabelecida como característica universal de toda Questão Narrativa. Também não existe uma referência genérica formada por tipo e identidade do objeto relacionado; as relações necessárias deverão permanecer explícitas nos recortes concretos à medida que forem compreendidas.

O enunciado não aceita texto vazio ou composto apenas por espaços. Os dados da questão são recebidos na construção e expostos por propriedades sem setter; a classe não gera o enunciado nem consulta o contexto.

A questão nasce com `answer` e `justification` iguais a `None`. O método `respond(answer, justification)` recebe uma resposta booleana e um `NarratorJustification`, mantendo ambos na questão. `False` representa uma resposta negativa, não ausência de resposta.

Cada questão aceita uma única resposta. Uma segunda tentativa lança `ValueError` e preserva a resposta e a justificativa originais, inclusive quando a primeira resposta foi `False`. Uma nova decisão exige outra questão. Os testes cobrem respostas positivas e negativas e a rejeição de uma segunda resposta.

Uma pergunta como "A condição ligada ao ritual de Borg continua pertinente após o ritual ter sido impedido?" solicita uma interpretação. Sua resposta não remove a condição nem modifica a configuração da Intenção. A questão guarda apenas a identidade da Intenção relacionada; não verifica a existência dessa Intenção nem executa consequências sobre ela.

### Relações já identificadas

Uma `NarrativeIntention` pode motivar Questões Narrativas em sua avaliação inicial de Intensidade e Pressão, em reavaliações posteriores e na interpretação da pertinência de condições antes da revisão de sua configuração de elegibilidade. Uma resposta de avaliação não seria booleana: seu conteúdo corresponde a Intensidade Narrativa, Pressão Narrativa e Justificativa do Narrador. Na avaliação inicial, esse julgamento é necessário antes de a Intenção estar completamente construída, pois a Intenção já recebe o resultado vigente em seu construtor. Portanto, mesmo quando uma identidade é reservada antecipadamente, a entidade relacionada à questão não precisa existir de forma completa no momento da formulação.

Uma `NarrativePreparation` participa em dois momentos diferentes. Antes de existir, ela pode ser produzida como consequência de uma solicitação criativa relacionada à Intenção elegível; a entidade de origem da questão e a entidade produzida pela resposta não são necessariamente a mesma. Depois de criada, a Preparação pode tornar-se o assunto das decisões discricionárias já descritas para adaptação, Avaliação de Oportunidade e Avaliação de Materialização.

`NarrativeIntensityAndPressureAssessmentRecord` não é o assunto da avaliação: ele registra uma ocorrência concluída. Se a avaliação for solicitada por uma Questão Narrativa, questão e registro representam fatos diferentes. A questão preserva o que foi solicitado e respondido; o registro preserva a identidade da ocorrência, o momento, o disparo, a Intenção avaliada e o resultado. A relação entre ambos ainda não está implementada e deverá evitar que resposta, resultado e justificativa se tornem fontes de verdade independentes e contraditórias.

Os Value Objects envolvidos não se tornam, por isso, proprietários de questões. `NarratorJustification` compõe a resposta; `NarrativeIntensityAndPressureAssessment` pode representar seu conteúdo estruturado; e `NarrativeEligibilityConfiguration` pode ser substituída como consequência posterior de uma decisão. A Avaliação de Elegibilidade permanece fora desse mecanismo porque é uma operação determinística do Tessitura, sem discricionariedade do Narrador.

### Limites da implementação atual

Ainda não existem geração automática de questões, recuperação progressiva de contexto L2/L3, respostas estruturadas além de `bool`, coordenação de questões encadeadas nem relações com Preparações ou registros de avaliação. A justificativa da resposta binária já pertence à questão; as justificativas dos assessments e das preparações existentes permanecem onde estão, sem migração automática neste recorte.

## Estágios de compromisso narrativo

Uma direção narrativa pode adquirir compromisso com a realidade do jogo progressivamente. Os conceitos descritos aqui não são camadas arquiteturais nem níveis de um único objeto: são conceitos distintos e relacionados.

O **Cânone da História** representa a verdade objetiva completa do mundo: tudo que aconteceu e tudo que está acontecendo, inclusive fatos que o Jogador ainda desconhece. Somente aquilo que se torna real pode alterar o Cânone da História.

### Intenção Narrativa

Uma Intenção Narrativa é uma direção desejada para a história que ainda possui pouco compromisso com a forma pela qual poderá acontecer. Ela deve possuir poucos atributos e permanecer altamente maleável. Ainda podem estar indefinidos seus participantes, seu alvo, seu momento, seu local e sua forma de realização.

Uma Intenção Narrativa pressiona o sistema para encontrar alguma forma coerente de realização, mas não garante que acontecerá. Espera-se que boa parte das Intenções seja realizada, diretamente ou por meio de combinação com outras, quando o sistema estiver funcionando adequadamente. Enquanto permanecer apenas como intenção, ela não altera o Cânone da História.

Uma Intenção possui identidade estável durante sua existência. Sua direção, sua Intensidade Narrativa, sua Pressão Narrativa e seu estado podem evoluir sem substituir essa identidade; alterar seu identificador não é uma transição válida.

O planejamento atual privilegia Intenções pequenas, normalmente realizáveis por uma única Situação. Intenções maiores, que precisem de várias Situações para serem cumpridas, permanecem como possibilidade para uma evolução futura do sistema.

Uma Intenção possui **Intensidade Narrativa** e **Pressão Narrativa**, que representam dimensões diferentes:

- **Intensidade Narrativa** expressa a força que sua realização deverá possuir. Uma Intenção forte pede uma manifestação intensa ou dramática; uma Intenção fraca pode produzir um acontecimento cotidiano, um pequeno revés ou outra manifestação simples.
- **Pressão Narrativa** expressa a urgência com que alguma realização deve ser encontrada. Ela pode aumentar enquanto uma Intenção elegível permanece aguardando materialização, sem transformar uma Intenção fraca em uma manifestação forte.

Uma Intenção pode ser completamente aberta ou possuir uma ou mais **âncoras narrativas**. Uma âncora liga a Intenção a uma origem, personagem, relação, acontecimento ou outro elemento do Cânone que suas Preparações deverão respeitar. Ela preserva a direção causal sem determinar necessariamente quem executará a Situação.

Uma Intenção de vingança ancorada em Borg, por exemplo, pode ser preparada por meio do próprio Borg, de sua esposa, de seu filho ou de mercenários contratados por ele. Uma pessoa sem relação causal com Borg não pode satisfazer essa Intenção apenas por produzir uma consequência superficialmente parecida.

Uma Intenção cumprida é encerrada e deixa de pressionar o sistema, abrindo espaço para outras. Uma Intenção que perde coerência ou permanece sem forma adequada pode ser transformada, combinada com outra ou encerrada sem realização.

### Avaliação e Reavaliação de Intensidade e Pressão

A Avaliação de Intensidade e Pressão estabelece os valores iniciais de uma Intenção Narrativa. A Reavaliação de Intensidade e Pressão reconsidera os valores de uma Intenção existente. Ambas são realizadas inteiramente pelo Narrador, que interpreta o contexto relevante, escolhe os valores e fornece uma Justificativa do Narrador.

Intensidade e Pressão podem aumentar, diminuir ou permanecer iguais em uma reavaliação, inclusive depois que a Intenção tiver originado Preparações Narrativas. As duas dimensões não precisam variar juntas nem no mesmo sentido. A passagem do tempo, mudanças nos recursos ou outros acontecimentos não determinam por si mesmos uma direção obrigatória de alteração. O Narrador deve escolher uma interpretação coerente com os personagens, as Âncoras Narrativas e o Cânone, sem pressupor uma única reação narrativamente correta.

Nessas avaliações, a responsabilidade do Tessitura é receber os dados e executar as validações determinísticas programadas. Tessitura não julga a interpretação do Narrador nem calcula qual reação narrativa deveria decorrer dos acontecimentos. A aplicação e o registro dos valores são operações distintas da avaliação narrativa.

Avaliação inicial e reavaliação representam momentos distintos da mesma atividade.

#### Resultado da avaliação

`NarrativeIntensityAndPressureAssessment` é o Value Object imutável que reúne Intensidade Narrativa, Pressão Narrativa e Justificativa do Narrador. Ele representa o resultado da avaliação, não o mecanismo que a realiza.

O resultado contém valores finais, não variações a somar ou subtrair. Os objetos que o compõem rejeitam intensidade ou pressão fora das faixas definidas abaixo e justificativa vazia ou composta apenas por espaços. Essas validações não julgam a coerência narrativa da decisão.

#### Escalas de Intensidade e Pressão

As faixas acordadas são inteiras e incluem seus limites:

- **Pressão Narrativa: de 0 a 100.** Zero representa ausência de urgência atual para buscar uma realização.
- **Intensidade Narrativa: de 1 a 100.** Toda Intenção possui alguma força de realização; zero não integra essa escala.

Os valores são pontos da escala do motor narrativo, não porcentagens nem probabilidades. As faixas permitem ajustes pequenos sem casas decimais e não exigem que intensidade e pressão variem juntas.

O Narrador escolhe os valores dentro dessas faixas. Cabe ao Tessitura rejeitar valores fora dos limites, sem arredondar ou ajustar silenciosamente uma entrada para o mínimo ou o máximo permitido.

Os limites estão implementados nos Value Objects: `NarrativePressure` rejeita valores fora de 0 a 100 e `NarrativeIntensity` rejeita valores fora de 1 a 100, lançando `ValueError` durante a construção. Os testes cobrem a aceitação dos extremos de cada faixa e a rejeição de valores abaixo do mínimo e acima do máximo.

#### Resultado vigente na Intenção

`NarrativeIntention` recebe um resultado na construção e o expõe pela propriedade `current_assessment`. As propriedades `intensity` e `pressure` consultam esse resultado, sem manter cópias independentes dos valores.

Uma Intenção pode passar por várias avaliações, mas mantém um único resultado vigente. O método `apply_assessment()` substitui o resultado completo, mantendo intensidade, pressão e justificativa da mesma avaliação juntas. Ele não modifica o resultado anterior nem cria um registro histórico automaticamente.

#### Registro de avaliação

`NarrativeIntensityAndPressureAssessmentRecord` representa uma ocorrência concluída de avaliação. É uma entidade imutável: resultados iguais podem pertencer a ocorrências distintas. Seus campos são:

- `id`: identidade do registro;
- `intention_id`: identidade da Intenção avaliada;
- `evaluated_at`: data e hora reais da avaliação, obrigatoriamente com fuso horário, distintas do tempo ficcional da campanha;
- `trigger`: categoria do disparo;
- `assessment`: resultado da avaliação, incluindo a justificativa do Narrador.

Vários registros podem se referir à mesma Intenção por `intention_id`. O registro é específico para avaliações de intensidade e pressão; ainda não existe um registro genérico para os outros tipos de avaliação.

Criar um registro não aplica seu resultado à Intenção. Da mesma forma, aplicar um resultado não o registra. Um registro de avaliação, isoladamente, não comprova que seu resultado foi aplicado.

#### Aplicação de uma avaliação registrada

`apply_recorded_narrative_assessment()` é um caso de uso implementado como função na camada de aplicação. Ele recebe uma Intenção e um registro já construídos, verifica se `record.intention_id` corresponde a `intention.id` e delega a substituição do resultado vigente a `NarrativeIntention.apply_assessment()`.

Um registro de outra Intenção é rejeitado com `ValueError` antes de qualquer substituição, preservando integralmente o resultado vigente. Quando a correspondência é válida, `current_assessment` passa a referenciar exatamente o resultado do registro recebido.

Em aplicações sucessivas, a Intenção fica com o último resultado aplicado; os registros anteriores preservam seus resultados e justificativas. O caso de uso não cria nem salva registros, não mantém uma coleção histórica e não verifica a ordem cronológica das avaliações. Aplicar um registro não significa persistir esse registro.

#### Categorias de disparo

O enum `EvaluationTriggerKind` representa as categorias de origem da avaliação:

| Categoria | Significado |
| --- | --- |
| `INITIAL_EVALUATION` | Avaliação inicial, que estabelece os primeiros valores. |
| `TIME_THRESHOLD_REACHED` | Um limite configurado de tempo ficcional foi atingido. |
| `LEVEL_THRESHOLD_REACHED` | Um limite configurado de nível foi atingido, seja individual ou da soma dos níveis do grupo. |
| `ANCHOR_STATE_CHANGED` | Mudaram campos relevantes para o motor narrativo no elemento ligado à Âncora Narrativa. |
| `KNOWLEDGE_CHANGED` | Houve mudança de conhecimento relevante, seja do elemento ligado à Âncora, seja do personagem do Jogador ou de seu grupo. |

Os disparos de reavaliação representam condições determinísticas cuja identificação cabe ao Tessitura, não interpretações do Narrador. Uma mudança de estado relevante significa uma mudança nos campos definidos para acompanhamento, não qualquer alteração no personagem, lugar, item ou outro elemento. Sinalizar uma reavaliação não determina seu resultado.

O enum identifica somente a categoria. Ele não contém a condição concreta, o limite configurado, os campos alterados, quem adquiriu informação ou qual informação foi adquirida.

#### Limites da implementação atual

Existem as representações do resultado, do registro e das categorias de disparo, além da substituição do resultado vigente na Intenção e do caso de uso que aplica o resultado de um registro correspondente. Ainda não existem monitoramento de condições, agendamento, persistência de histórico ou coordenação automática entre criar um registro e aplicar uma avaliação.

O fornecimento de contexto em níveis de aprofundamento sob demanda continua sendo uma hipótese de apoio ao fluxo, não um mecanismo implementado.

### Avaliação de Elegibilidade

Antes de produzir Preparações Narrativas, uma Intenção deve passar por uma Avaliação de Elegibilidade executada inteiramente pelo Tessitura. A avaliação aplica Critérios de Elegibilidade estruturados ao Cânone da História e ao estado atual da Intenção.

A Avaliação de Elegibilidade é uma operação pura, determinística e idempotente para os mesmos dados. Ela pode ser repetida sem participação do Narrador e sem consumo de tokens. Uma mudança no tempo ficcional, no Estado do Mundo, na Pressão Narrativa, nas Âncoras Narrativas ou em outro dado relevante representa uma nova entrada e pode produzir um resultado diferente.

Tessitura não precisa avaliar continuamente todas as Intenções. No modelo acordado, toda mudança em um campo acompanhado solicita a reavaliação das Intenções vinculadas àquela condição, inclusive quando a mudança faz uma condição deixar de ser satisfeita. O resultado positivo estabelece que a Intenção está elegível, mas não cria Preparações Narrativas.

O Narrador é responsável por transformar uma Intenção Elegível em uma ou várias Preparações Narrativas. Como a Avaliação de Elegibilidade não envolve discricionariedade do Narrador, ela não exige uma Justificativa do Narrador. Tessitura pode manter diagnósticos estruturados para auditoria ou depuração sem convertê-los em prosa destinada à IA.

#### Criação e revisão da configuração de elegibilidade

Uma Intenção deve nascer com uma configuração de elegibilidade que contenha ao menos uma condição obrigatória ou ponderada. `NarrativeIntention` exige o argumento `eligibility_configuration` na construção e preserva essa configuração em uma propriedade sem setter. A ausência completa de condições é rejeitada durante a construção da configuração, antes de sua entrega à Intenção; não representa elegibilidade automática nem uma condição temporária de inelegibilidade.

`NarrativeEligibilityConfiguration` é um Value Object imutável com três campos: `mandatory_conditions`, uma tupla de condições obrigatórias; `weighted_conditions`, uma tupla de pares `(condição, peso)`; e `minimum_score`, a pontuação mínima. Rejeita ausência completa de condições, pesos negativos e pontuação mínima negativa com `ValueError`. Inicialmente, ambas as categorias aceitam apenas `MinimumNarrativePressureCondition`, a única condição concreta implementada.

Os testes protegem as configurações inválidas e o vínculo da Intenção com a configuração recebida, impedindo sua substituição direta. Receber uma configuração não exige que suas condições estejam satisfeitas naquele momento nem executa automaticamente uma avaliação.

A configuração descreve as regras cadastradas, como "nível mínimo 5", e os parâmetros da combinação. Os booleanos recebidos por `evaluate_narrative_eligibility()` são resultados da verificação dessas regras em um momento específico, não a configuração em si. Cadastrar as condições na criação não significa congelar seus resultados: mudanças nos dados acompanhados podem mudar esses resultados.

As próprias regras também podem precisar de revisão. Uma condição que dependesse de um ritual impedido pelo Jogador poderia deixar de ser pertinente, sem que a Intenção perdesse seu sentido. Esse exemplo motiva a revisão, mas condições sobre rituais ainda não estão representadas no código.

`NarrativeIntention.revise_eligibility_configuration()` recebe uma nova configuração válida e substitui a referência vigente, sem modificar a configuração anterior, a identidade da Intenção ou seu resultado de intensidade e pressão. A propriedade continua sem setter. Imutabilidade da configuração não significa que a Intenção precise conservar a mesma configuração para sempre.

A construção da nova configuração executa novamente suas validações. Se falhar por ausência de condições, peso negativo ou pontuação mínima negativa, a chamada de revisão não acontece e a configuração vigente permanece intacta. Os testes protegem a revisão válida, essas falhas de construção e a imutabilidade dos três campos da configuração.

A revisão exige uma mudança explícita: o Tessitura não decide automaticamente quais regras perderam sentido. O método não registra histórico ou justificativa da revisão e não executa a avaliação de elegibilidade.

#### Condições acompanhadas

O modelo acordado considera as seguintes condições, conforme sua pertinência para cada Intenção:

- **Pressão Narrativa:** comparação da pressão vigente com um limite configurado.
- **Distância física:** comparação entre referências espaciais definidas e um limite configurado de distância.
- **Janela de tempo ficcional:** uma data foi alcançada ou o momento atual está dentro de um intervalo definido.
- **Nível do personagem ou do grupo:** um nível individual ou a soma dos níveis do grupo atingiu um limite configurado.
- **Estado de elementos ligados às âncoras:** campos estruturados satisfazem condições explícitas, como um personagem estar vivo ou livre e uma passagem estar aberta.
- **Pré-requisitos canônicos:** um acontecimento identificado ocorreu ou uma informação específica está registrada como conhecida por determinado personagem ou grupo.
- **Disponibilidade de recursos:** quantidades registradas, como soldados, dinheiro ou cargas de um artefato, satisfazem limites definidos.
- **Intervalo desde uma ocorrência anterior:** passou o tempo ficcional configurado desde uma preparação ou situação associada à Intenção.

Todas essas categorias podem ser acompanhadas; cada Intenção usa apenas as condições pertinentes a ela. O acompanhamento identifica mudanças nos dados utilizados pelas condições, não apenas a passagem de um resultado falso para verdadeiro. Avanços de tempo e deslocamentos também podem alterar essas entradas.

O disparo solicita uma nova verificação; não comprova a elegibilidade. Não há necessidade de um primeiro nível de pontuação para autorizar a avaliação: a mudança acompanhada já a solicita. Reavaliar a elegibilidade não recalcula intensidade ou pressão nem solicita, por si só, uma nova interpretação do Narrador.

#### Limite padrão da condição de pressão

O limite padrão acordado é **50**, configurável por Intenção por meio de suas condições cadastradas. A condição de pressão é satisfeita quando a pressão vigente é **maior ou igual ao limite configurado**. O valor 50 é uma hipótese inicial, revisável conforme a experiência em campanhas, e está implementado como padrão da condição concreta.

`MinimumNarrativePressureCondition` é um Value Object imutável no domínio. Seu campo `minimum` contém um `NarrativePressure`, com padrão 50, e aceita um limite personalizado representado pelo mesmo tipo. Assim, o limite utiliza a faixa válida de pressão, de 0 a 100.

O método `is_satisfied_by(pressure)` recebe um `NarrativePressure` e retorna o resultado de `pressure.value >= minimum.value`, sem consultar nem alterar a Intenção. A condição representa a regra cadastrada; o booleano retornado representa o resultado de uma verificação. Os testes cobrem a configuração padrão e personalizada e a comparação abaixo, exatamente no limite e acima dele.

A condição pode ser incluída entre as obrigatórias ou, acompanhada de seu peso, entre as ponderadas de `NarrativeEligibilityConfiguration`. A condição não dispara avaliações automaticamente nem decide sozinha a elegibilidade completa.

Esse limite não impede reavaliações abaixo dele. Com o padrão de 50, uma mudança de 30 para 40 solicita reavaliação, mas mantém a condição falsa; de 49 para 50, torna a condição verdadeira; de 50 para 49, torna-a falsa novamente. Todas essas mudanças solicitam reavaliação quando a pressão é acompanhada.

A condição pode contribuir com seu peso ou funcionar como requisito obrigatório, conforme a configuração da Intenção. Atingir 50 não garante, isoladamente, a elegibilidade, e esse valor não define a pontuação mínima da soma ponderada.

#### Condições obrigatórias e ponderadas

Uma condição pode funcionar como requisito obrigatório ou como contribuição ponderada. As condições obrigatórias precisam estar todas satisfeitas e não acrescentam pontos. Nenhuma pontuação compensa um requisito obrigatório não satisfeito.

Cada condição ponderada satisfeita acrescenta seu peso à pontuação; uma condição não satisfeita acrescenta zero. O cálculo recebe pesos e pontuação mínima inteiros não negativos. A regra de combinação é:

> Uma Intenção está elegível quando todas as condições obrigatórias estão satisfeitas e a soma dos pesos das condições ponderadas satisfeitas é maior ou igual à pontuação mínima configurada.

O Tessitura executa essa configuração de forma determinística. Ele não interpreta a história para inventar pesos, limites ou obrigatoriedades durante a avaliação.

#### Referências espaciais

A distância considerada é física, calculável a partir de dados espaciais estruturados, e não uma interpretação de "distância narrativa". Cada condição de distância precisa identificar as referências comparadas e o limite aplicável. A representação dos mapas e o sistema de coordenadas ainda não foram definidos.

Não se exige uma coordenada própria e única para toda Âncora Narrativa. Um item carregado pode acompanhar a posição do portador; uma doença ou catástrofe pode estar associada a uma área; certas âncoras podem não ter uma posição física pertinente à avaliação.

Proximidade não é obrigatória para toda Intenção. Borg pode enviar mercenários mesmo estando distante, de modo que a proximidade com ele pode ter pouco peso ou nem participar das condições. Já uma possibilidade de contrair uma doença exclusivamente em determinado pântano pode exigir presença naquela área como condição obrigatória, impossível de compensar com pressão alta.

#### Limites da implementação de elegibilidade

`evaluate_narrative_eligibility()` implementa a regra de combinação como uma função pura no domínio, não como um caso de uso. Ela recebe `mandatory_conditions`, uma sequência de resultados booleanos; `weighted_conditions`, uma sequência de pares `(condição_satisfeita, peso)`; e `minimum_score`, a pontuação mínima. Retorna `True` quando todas as obrigatórias estão satisfeitas e a soma dos pesos das ponderadas satisfeitas alcança ou supera o limite; caso contrário, retorna `False`.

A função rejeita pesos ou pontuação mínima negativos com `ValueError`, mesmo quando uma condição obrigatória não está satisfeita. Pesos de condições ponderadas falsas também são validados, embora não contribuam para a pontuação.

Com ambas as sequências vazias, a função lança `ValueError`, inclusive quando a pontuação mínima é zero. Ter somente condições obrigatórias ou somente ponderadas continua permitido: sem obrigatórias não há bloqueio obrigatório; sem ponderadas a pontuação é zero, mas as obrigatórias ainda precisam ser satisfeitas. A ausência de condições é uma entrada inválida, distinta de condições existentes que não foram satisfeitas.

Os testes cobrem bloqueio obrigatório apesar de pontuação suficiente, pontuação abaixo, igual e acima do limite, ausência de contribuição de condições falsas, rejeição de configurações negativas e de ausência completa de condições, além da avaliação com uma única categoria de condições.

`NarrativeIntention` já exige uma `NarrativeEligibilityConfiguration` com condições cadastradas. Ainda não existe uma operação que percorra essa configuração, verifique todas as condições e encaminhe seus resultados a `evaluate_narrative_eligibility()`. A função permanece independente da configuração: rejeita a ausência completa de resultados, mas não confere se uma lista parcialmente preenchida contém todas as condições esperadas para a Intenção.

Essa função não consulta o mundo, não acompanha mudanças, não modifica a Intenção e não cria Preparações. A obtenção dos dados, as demais condições concretas, os mapas e a identificação das Intenções afetadas permanecem pendentes. O limite padrão de pressão 50 não é aplicado por essa função: comparar pressão e limite pertence a `MinimumNarrativePressureCondition.is_satisfied_by()`, cuja verificação é anterior à combinação dos resultados.

### Preparação Narrativa

Uma Preparação Narrativa é uma forma mais concreta pela qual uma Intenção Narrativa pode materializar-se. Ela possui mais atributos que a Intenção e pode começar a definir participantes, alvos, lugares, períodos, condições, gatilhos e formas de entrada na realidade.

Uma Preparação continua sendo uma possibilidade, não um fato. Ela permanece maleável, embora menos que a Intenção que a originou. O Narrador pode adaptá-la ao reconhecer uma oportunidade mais adequada, desde que a alteração respeite o Cânone e os compromissos que já tenham se tornado reais.

Cada Preparação é filha de uma única Intenção Narrativa, mas uma Intenção pode desdobrar-se em várias Preparações alternativas, como uma missão paralela, uma interrupção de intenção declarada ou outra situação compatível com sua direção.

Uma Preparação também possui identidade estável. Adaptações preservam tanto essa identidade quanto a Intenção Narrativa que a originou; substituir qualquer uma delas não é uma adaptação válida.

Para uma Intenção pequena, é provável que apenas uma de suas Preparações alternativas precise tornar-se uma Situação. As demais devem ser reavaliadas ou encerradas quando perderem sua finalidade. Uma mesma Situação pode, entretanto, materializar Preparações compatíveis oriundas de Intenções diferentes.

Uma Preparação não altera por si mesma o Cânone da História.

A criação de uma Preparação é uma decisão criativa do Narrador. Cada Preparação criada deve conter uma Justificativa do Narrador que explique brevemente como aquela forma realiza a direção da Intenção, respeita suas Âncoras Narrativas e corresponde à Intensidade Narrativa pretendida.

### Oportunidade Narrativa

Uma Oportunidade Narrativa surge quando o contexto atual satisfaz os Requisitos Rígidos e ao menos parte dos Requisitos Maleáveis de uma Preparação, permitindo considerar sua adaptação ao momento presente. A Oportunidade não é uma passagem obrigatória: uma Preparação que já encontre a forma esperada pode seguir diretamente para uma Avaliação de Materialização.

Tessitura deve procurar correspondências entre Preparações e o Estado do Mundo, descartar incompatibilidades mecanicamente verificáveis e reunir Evidências de Oportunidade relevantes. Essas evidências podem incluir Fatos Canônicos, estados de participantes, localizações, relações, recursos e condições satisfeitas ou ausentes.

O Narrador conduz a Avaliação de Oportunidade seguindo um roteiro explícito: verifica os Requisitos Rígidos, examina quais Requisitos Maleáveis foram satisfeitos, consulta as evidências reunidas e pesquisa partes adicionais do Cânone quando necessário. Ao final, decide rejeitar a Oportunidade, aceitar a Preparação sem alterações ou propor uma adaptação.

Uma adaptação pode alterar apenas elementos maleáveis. Ela não pode romper Âncoras Narrativas, modificar Fatos Canônicos nem ocultar um Requisito Rígido ausente. A Avaliação de Oportunidade e toda adaptação resultante devem conter Justificativas do Narrador em prosa curta.

### Avaliação de Materialização e Materialização

Antes de uma Preparação ingressar na realidade, ela deve passar por uma Avaliação de Materialização realizada em conjunto pelo Tessitura e pelo Narrador.

Tessitura realiza a parte mecanicamente verificável. Ele examina Requisitos Rígidos, Âncoras Narrativas, Fatos Canônicos, estados e localizações dos participantes, recursos necessários, compatibilidade temporal e conflitos com outras Situações. Seu resultado identifica Bloqueios de Materialização, apresenta alertas ou informa que nenhum impedimento mecânico foi encontrado.

O Narrador avalia a parte semântica: decide se a forma final ainda realiza a Intenção, se sua Intensidade Narrativa está adequada e se aquele é um momento narrativamente apropriado. Diante do resultado conjunto, pode descartar a Preparação, corrigi-la ou aprová-la. Toda decisão discricionária tomada nessa avaliação deve conter uma Justificativa do Narrador.

A Avaliação de Materialização não altera o Cânone da História. A Materialização é uma operação posterior e mutável, solicitada pelo Narrador depois da aprovação. A solicitação deve conter uma Justificativa do Narrador que explique por que a Preparação deve ingressar na realidade naquele momento.

Tessitura executa a Materialização de forma controlada, cria a Situação e impede que a mesma solicitação produza Situações duplicadas. Depois desse limite, a nova circunstância pertence à realidade do jogo e não pode simplesmente retornar ao estado de Preparação.

### Situação

Uma Situação surge quando uma ou mais Preparações compatíveis são confirmadas como apropriadas e ingressam na realidade do jogo. A partir desse momento, a Situação interage com o estado do mundo e com as ações do Jogador, sem que seu resultado esteja predeterminado pelas Intenções que a originaram.

A Situação existe apenas enquanto aquela circunstância está ativa no mundo. Quando se resolve, ela produz fatos canônicos imutáveis e alterações no estado atual. O estado pode voltar a mudar por meio de novos acontecimentos, mas os fatos que produziram seus estados anteriores continuam pertencendo ao Cânone da História.

Ao término da Situação, as Intenções que contribuíram para ela devem ser avaliadas. Aquelas cujos critérios de cumprimento foram atendidos são encerradas e deixam de exercer Pressão Narrativa; as demais podem continuar, transformar-se ou gerar novas Preparações.

### Fluxo de cima para baixo

O fluxo de cima para baixo descreve a aquisição progressiva de forma e compromisso com a realidade:

```text
Intenção Narrativa
        ↓ Avaliação de Elegibilidade pelo Tessitura
Intenção Elegível
        ↓ criação pelo Narrador + justificativa
Preparações Narrativas
        ↓ Oportunidade Narrativa opcional
Preparações adaptadas
        ↓ Avaliação de Materialização
Preparações aprovadas
        ↓ Materialização + justificativa
Situação
        ↓ produz
Fatos canônicos e alterações no estado do mundo
```

### Fluxo de baixo para cima

O fluxo de baixo para cima descreve como acontecimentos reais alimentam novas direções narrativas.

Uma consequência pode primeiro alterar o estado mental de um personagem. Se o Jogador fere Borg e foge, por exemplo, o desejo de vingança de Borg torna-se um fato canônico sobre esse personagem, mesmo que o Jogador o desconheça. A partir dessa realidade pode surgir uma nova Intenção Narrativa ancorada em Borg, capaz de gerar Preparações coerentes com sua personalidade, seus recursos e suas relações.

```text
Situação
        ↓ produz
Fatos canônicos e novo estado do mundo
        ↓ provocam
Intenções de personagens e novas direções narrativas
        ↓ podem originar
Novas Intenções Narrativas
```

A intenção de um personagem e uma Intenção Narrativa continuam sendo conceitos diferentes. A primeira é um fato canônico sobre aquilo que o personagem deseja; a segunda é uma direção ainda não realizada para a história. Uma pode originar a outra por meio de uma âncora narrativa.

As Intenções não formam necessariamente uma fila simples. Intensidade Narrativa, Pressão Narrativa, coerência com o Cânone e adequação das Preparações ajudam a determinar quais direções encontram oportunidade de materialização primeiro. O mecanismo exato dessa avaliação ainda não foi estabelecido.

### Divisão entre determinação e discricionariedade

Tessitura assume o trabalho que pode ser expresso por regras estáveis sobre estado estruturado: avaliações puras, cálculos, progressão temporal, validação de requisitos, detecção de conflitos, recuperação de evidências e aplicação controlada de mudanças.

O Narrador assume o trabalho que exige interpretação semântica e escolha entre várias soluções narrativamente válidas: criação de Preparações, reconhecimento da relevância de uma Oportunidade, adaptação de elementos maleáveis e confirmação da entrada de uma Preparação na realidade.

Sempre que o Narrador participa de uma decisão, ele deve fornecer uma Justificativa do Narrador em uma ou duas frases. A justificativa é persistida com a decisão para permitir auditoria e formar material capaz de orientar melhorias futuras no Tessitura. Operações realizadas exclusivamente pelo Tessitura não exigem justificativa em prosa; seus resultados devem decorrer deterministicamente dos mesmos dados.

Depois que uma Situação ingressa na realidade, consequências puramente mecânicas podem ser resolvidas pelo Tessitura sem nova mediação do Narrador. A intervenção da IA é reservada aos pontos em que existe uma escolha semântica legítima.
