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

**Interrupção de intenção:** ocorrência durante um avanço narrativo que impede ou torna inadequada a continuação automática de uma ou mais intenções ainda não realizadas do Jogador. A interrupção encerra o avanço e cria um novo ponto de interação para que o Jogador possa reavaliar suas ações.

## Responsabilidades pretendidas

Tessitura deverá assumir o máximo possível do trabalho operacional necessário para conduzir a campanha. Sua responsabilidade não estará limitada ao armazenamento e à consulta de informações: também deverá administrar o estado e parte significativa da lógica do mundo.

A CLI deverá oferecer comandos e subcomandos relacionados a áreas como campanha, Jogador, NPCs e mundo. Entre outras operações, deverá permitir consultar e modificar atributos, localizações, relações e demais informações relevantes para a continuidade da campanha.

Tessitura também deverá avaliar acontecimentos do mundo e suas consequências. Isso inclui, por exemplo, determinar se um encontro deve ocorrer e quais consequências decorrem do sucesso ou fracasso de uma missão.

Os comandos e subcomandos mencionados aqui são exemplos da direção pretendida. Sua organização definitiva ainda não foi estabelecida.

## Estágios de compromisso narrativo

Uma direção narrativa pode adquirir compromisso com a realidade do jogo progressivamente. Os estágios descritos aqui não são camadas arquiteturais: representam estados conceituais pelos quais uma direção narrativa pode passar.

O **Cânone da História** representa a verdade objetiva completa do mundo: tudo que aconteceu e tudo que está acontecendo, inclusive fatos que o Jogador ainda desconhece. Somente aquilo que se torna real pode alterar o Cânone da História.

### Intenção narrativa

Uma intenção narrativa é uma direção desejada para a história que ainda não entrou em preparação. Ela pode possuir condições que indiquem quando se tornará elegível para preparação, como data, período, local, horário, nível ou condição do personagem.

Uma intenção narrativa não afirma que algo aconteceu nem garante que acontecerá. Enquanto permanecer nesse estágio, ela não altera o Cânone da História.

### Preparação narrativa

Uma preparação narrativa é uma intenção cujas condições de elegibilidade foram suficientemente atendidas para que formas concretas de introduzi-la no mundo comecem a ser avaliadas.

Durante esse estágio, podem ser consideradas oportunidades como uma missão paralela, um deslocamento do personagem ou uma interrupção de intenção. A situação ainda não é real e, por isso, sua preparação não altera por si mesma o Cânone da História.

### Situação em curso

Uma situação em curso surge quando uma preparação é confirmada como apropriada para acontecer e ingressa na realidade do jogo. A partir desse momento, ela interage com o estado do mundo e com as ações do Jogador, sem que seu resultado esteja predeterminado pela intenção que a originou.

As ocorrências e consequências produzidas durante uma situação em curso alteram o estado atual e passam a compor o Cânone da História. Quando a situação deixa de estar em curso, os fatos que ela produziu continuam pertencendo ao cânone.
