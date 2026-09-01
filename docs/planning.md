# Tessitura: Ideias centrais

## Vocabulário

**Tessitura:** aplicação de linha de comando disponibilizada ao Agente Narrador para apoiar a condução de uma campanha de D&D 5.5e para um Jogador.

**Jogador:** pessoa que participa da campanha e declara, por meio de mensagens ao Narrador, as falas, ações e escolhas sob seu controle.

**Narrador:** agente de IA configurado com acesso ao Tessitura e responsável por conduzir a narrativa da campanha, comunicar consequências, representar NPCs e apresentar acontecimentos relevantes do mundo.

**Ponto de interação:** fronteira da progressão narrativa na qual a campanha permanece pausada até que o Jogador ou o Narrador forneça a manifestação necessária para continuar.

**Declaração do Jogador:** mensagem que comunica uma ou mais falas, ações, escolhas ou intenções do Jogador. Pode abranger desde uma ação imediata até um plano que se estenda por um período maior de tempo ficcional.

**Resposta do Narrador:** mensagem que relata as consequências já produzidas, as ações de NPCs e as condições relevantes do mundo, conduzindo a narrativa até o próximo ponto de interação.

**Interação:** troca composta por uma declaração e pela resposta correspondente entre Jogador e Narrador.

**Avanço narrativo:** progressão ocorrida entre dois pontos de interação. Pode abranger um turno, vários turnos, minutos, horas ou dias de tempo ficcional.

**Interrupção de intenção declarada:** ocorrência durante um avanço narrativo que impede ou torna inadequada a continuação automática de uma ou mais ações expressas na Declaração do Jogador. A interrupção encerra o avanço e cria um novo ponto de interação para que o Jogador possa reavaliar suas ações.

**Cânone da História:** verdade objetiva completa do mundo, formada por tudo que aconteceu e tudo que está acontecendo, inclusive fatos que o Jogador desconhece.

**Intenção Narrativa:** direção ainda pouco comprometida com sua forma de realização. Ela pressiona o sistema para encontrar uma realização coerente, mas não pertence ao Cânone da História nem garante que acontecerá.

**Intensidade Narrativa:** escala ou força que a realização de uma Intenção Narrativa deverá possuir.

**Pressão Narrativa:** urgência com que o sistema deve procurar uma realização para uma Intenção Narrativa, sem alterar sua Intensidade Narrativa.

**Âncora Narrativa:** vínculo opcional entre uma Intenção Narrativa e um ou mais elementos do Cânone da História que devem permanecer causalmente relacionados às suas possíveis realizações. A âncora restringe a direção das Preparações Narrativas sem determinar necessariamente quem executará a Situação.

**Preparação Narrativa:** forma concreta possível de materializar uma única Intenção Narrativa. Ela pode definir participantes, alvos, lugares, condições e gatilhos, mas ainda não pertence ao Cânone da História.

**Situação:** circunstância que ingressou na realidade e permanece ativa enquanto interage com o Estado do Mundo e com as ações do Jogador. Pode materializar Preparações Narrativas compatíveis de diferentes Intenções Narrativas e atravessar vários avanços narrativos e pontos de interação.

**Fato Canônico:** afirmação imutável sobre algo que efetivamente aconteceu no mundo.

**Estado do Mundo:** condição atual do mundo, produzida pelos Fatos Canônicos acumulados e alterável por novos acontecimentos.

**Intenção de Personagem:** desejo ou objetivo pertencente a um personagem do mundo e, portanto, integrante do Cânone da História, mesmo quando desconhecido pelo Jogador. Pode originar uma Intenção Narrativa por meio de uma Âncora Narrativa.

## Responsabilidades pretendidas

Tessitura deverá assumir o máximo possível do trabalho operacional necessário para conduzir a campanha. Sua responsabilidade não estará limitada ao armazenamento e à consulta de informações: também deverá administrar o estado e parte significativa da lógica do mundo.

A CLI deverá oferecer comandos e subcomandos relacionados a áreas como campanha, Jogador, NPCs e mundo. Entre outras operações, deverá permitir consultar e modificar atributos, localizações, relações e demais informações relevantes para a continuidade da campanha.

Tessitura também deverá avaliar acontecimentos do mundo e suas consequências. Isso inclui, por exemplo, determinar se um encontro deve ocorrer e quais consequências decorrem do sucesso ou fracasso de uma missão.

Os comandos e subcomandos mencionados aqui são exemplos da direção pretendida. Sua organização definitiva ainda não foi estabelecida.

## Estágios de compromisso narrativo

Uma direção narrativa pode adquirir compromisso com a realidade do jogo progressivamente. Os conceitos descritos aqui não são camadas arquiteturais nem níveis de um único objeto: são conceitos distintos e relacionados.

O **Cânone da História** representa a verdade objetiva completa do mundo: tudo que aconteceu e tudo que está acontecendo, inclusive fatos que o Jogador ainda desconhece. Somente aquilo que se torna real pode alterar o Cânone da História.

### Intenção Narrativa

Uma Intenção Narrativa é uma direção desejada para a história que ainda possui pouco compromisso com a forma pela qual poderá acontecer. Ela deve possuir poucos atributos e permanecer altamente maleável. Ainda podem estar indefinidos seus participantes, seu alvo, seu momento, seu local e sua forma de realização.

Uma Intenção Narrativa pressiona o sistema para encontrar alguma forma coerente de realização, mas não garante que acontecerá. Espera-se que boa parte das Intenções seja realizada, diretamente ou por meio de combinação com outras, quando o sistema estiver funcionando adequadamente. Enquanto permanecer apenas como intenção, ela não altera o Cânone da História.

O planejamento atual privilegia Intenções pequenas, normalmente realizáveis por uma única Situação. Intenções maiores, que precisem de várias Situações para serem cumpridas, permanecem como possibilidade para uma evolução futura do sistema.

Uma Intenção possui **Intensidade Narrativa** e **Pressão Narrativa**, que representam dimensões diferentes:

- **Intensidade Narrativa** expressa a força que sua realização deverá possuir. Uma Intenção forte pede uma manifestação intensa ou dramática; uma Intenção fraca pode produzir um acontecimento cotidiano, um pequeno revés ou outra manifestação simples.
- **Pressão Narrativa** expressa a urgência com que alguma realização deve ser encontrada. Ela pode aumentar enquanto uma Intenção elegível permanece aguardando materialização, sem transformar uma Intenção fraca em uma manifestação forte.

Uma Intenção pode ser completamente aberta ou possuir uma ou mais **âncoras narrativas**. Uma âncora liga a Intenção a uma origem, personagem, relação, acontecimento ou outro elemento do Cânone que suas Preparações deverão respeitar. Ela preserva a direção causal sem determinar necessariamente quem executará a Situação.

Uma Intenção de vingança ancorada em Borg, por exemplo, pode ser preparada por meio do próprio Borg, de sua esposa, de seu filho ou de mercenários contratados por ele. Uma pessoa sem relação causal com Borg não pode satisfazer essa Intenção apenas por produzir uma consequência superficialmente parecida.

Uma Intenção cumprida é encerrada e deixa de pressionar o sistema, abrindo espaço para outras. Uma Intenção que perde coerência ou permanece sem forma adequada pode ser transformada, combinada com outra ou encerrada sem realização.

### Preparação Narrativa

Uma Preparação Narrativa é uma forma mais concreta pela qual uma Intenção Narrativa pode materializar-se. Ela possui mais atributos que a Intenção e pode começar a definir participantes, alvos, lugares, períodos, condições, gatilhos e formas de entrada na realidade.

Uma Preparação continua sendo uma possibilidade, não um fato. Ela permanece maleável, embora menos que a Intenção que a originou. O Narrador pode adaptá-la ao reconhecer uma oportunidade mais adequada, desde que a alteração respeite o Cânone e os compromissos que já tenham se tornado reais.

Cada Preparação é filha de uma única Intenção Narrativa, mas uma Intenção pode desdobrar-se em várias Preparações alternativas, como uma missão paralela, uma interrupção de intenção declarada ou outra situação compatível com sua direção.

Para uma Intenção pequena, é provável que apenas uma de suas Preparações alternativas precise tornar-se uma Situação. As demais devem ser reavaliadas ou encerradas quando perderem sua finalidade. Uma mesma Situação pode, entretanto, materializar Preparações compatíveis oriundas de Intenções diferentes.

Uma Preparação não altera por si mesma o Cânone da História.

### Situação

Uma Situação surge quando uma ou mais Preparações compatíveis são confirmadas como apropriadas e ingressam na realidade do jogo. A partir desse momento, a Situação interage com o estado do mundo e com as ações do Jogador, sem que seu resultado esteja predeterminado pelas Intenções que a originaram.

A Situação existe apenas enquanto aquela circunstância está ativa no mundo. Quando se resolve, ela produz fatos canônicos imutáveis e alterações no estado atual. O estado pode voltar a mudar por meio de novos acontecimentos, mas os fatos que produziram seus estados anteriores continuam pertencendo ao Cânone da História.

Ao término da Situação, as Intenções que contribuíram para ela devem ser avaliadas. Aquelas cujos critérios de cumprimento foram atendidos são encerradas e deixam de exercer Pressão Narrativa; as demais podem continuar, transformar-se ou gerar novas Preparações.

### Fluxo de cima para baixo

O fluxo de cima para baixo descreve a aquisição progressiva de forma e compromisso com a realidade:

```text
Intenção Narrativa
        ↓ desdobra
Preparações Narrativas
        ↓ materializam
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
