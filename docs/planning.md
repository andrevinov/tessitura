# Tessitura: Ideias centrais

## Responsabilidades pretendidas

Tessitura deverá assumir o máximo possível do trabalho operacional necessário para conduzir a campanha. Sua responsabilidade não estará limitada ao armazenamento e à consulta de informações: também deverá administrar o estado e parte significativa da lógica do mundo.

A CLI deverá oferecer comandos e subcomandos relacionados a áreas como campanha, Jogador, NPCs e mundo. Entre outras operações, deverá permitir consultar e modificar atributos, localizações, relações e demais informações relevantes para a continuidade da campanha.

Tessitura também deverá avaliar acontecimentos do mundo e suas consequências. Isso inclui, por exemplo, determinar se um encontro deve ocorrer e quais consequências decorrem do sucesso ou fracasso de uma missão.

Os comandos e subcomandos mencionados aqui são exemplos da direção pretendida. Sua organização definitiva ainda não foi estabelecida.

## Princípio de mediação

Tessitura deverá combinar um núcleo determinístico com a discricionariedade narrativa da IA. Tudo que puder ser expresso como regra estável sobre estado estruturado deverá, preferencialmente, ser resolvido pelo próprio Tessitura. Operações puras deverão produzir o mesmo resultado para os mesmos dados e não deverão consumir tokens nem exigir uma Justificativa do Narrador.

O Narrador deverá participar quando a decisão exigir interpretação semântica, adaptação contextual ou escolha entre várias soluções narrativamente válidas. Tessitura deverá recuperar apenas as informações relevantes, apresentar evidências quando necessárias, validar as decisões recebidas e controlar sua entrada na realidade do jogo.

Sempre que o Narrador criar, adaptar, avaliar, bloquear, descartar ou confirmar algo discricionariamente, deverá fornecer uma Justificativa do Narrador em prosa curta. Essas justificativas deverão ser persistidas para permitir auditoria das decisões e fornecer material para melhorar o Tessitura no longo prazo.

## Motor narrativo

O motor narrativo é um dos motores previstos para o Tessitura. Ele deverá apoiar a evolução de direções narrativas em possibilidades concretas e sua entrada controlada na realidade da campanha, preservando o Cânone e a liberdade de ação do Jogador. Seu funcionamento combinará operações determinísticas do Tessitura com decisões discricionárias do Narrador, conforme o princípio de mediação.

Os conceitos e as responsabilidades desse motor estão descritos no [modelo de compromisso narrativo](domain/narrative-commitment.md).
