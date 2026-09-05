# Roadmap de desenvolvimento

> Status: hipótese de implementação.

Este roadmap organiza a melhor compreensão atual sobre o caminho do Tessitura até uma primeira publicação beta. Ele orienta a ordem das investigações e explicita os marcos que permitirão avaliar progresso arquitetural.

O roadmap não autoriza a implementação automática de nenhum item. Cada classe, função, teste, integração, dependência e alteração documental continua exigindo proposta, compreensão, autorização, implementação, verificação e revisão próprias.

O plano é revisável. Código implementado e experimentos executados constituem evidência; itens futuros permanecem hipóteses.

## Direção do produto

Tessitura deverá ser um motor determinístico de campanha que trabalha em conjunto com uma IA Narradora. O núcleo não deverá depender de um fornecedor específico de IA, de um cliente específico nem da presença da campanha dentro de um repositório Git.

Conceitualmente, a direção atual é:

```text
Narrador escolhido pelo usuário
              ↓
adaptador externo: CLI, MCP, API ou outro
              ↓
contrato de acesso progressivo
              ↓
núcleo narrativo e regras de D&D
              ↓
estado e material da campanha
```

O modo "repositório clonado + agente CLI" continuará sendo útil para desenvolvimento, diagnóstico e comparação com a experiência anterior. Ele não deverá definir sozinho o formato do produto.

A campanha deverá poder existir separadamente do código-fonte do Tessitura. A política de contexto, as regras e o estado canônico deverão pertencer ao Tessitura; um adaptador apenas os transportará entre a aplicação e o Narrador.

## Ritmo dentro dos marcos

Cada marco contém muitas unidades conceituais. O trabalho dentro dele continuará incremental, seguindo um ritmo como:

```text
uma unidade de código
        ↓
um teste significativo
        ↓
revisão e checkpoint
        ↓
próxima unidade autorizada
        ↓
teste de interação quando dois conceitos criarem essa pressão
```

Uma classe não autoriza seus futuros métodos. Um comportamento não autoriza todos os seus testes. Uma segunda classe não autoriza automaticamente um teste de integração. Cada um continua sendo uma unidade independente.

Ao atingir um marco, o roadmap deverá ser reavaliado antes de avançar. Uma contradição que impeça a unidade atual também poderá provocar uma reavaliação antecipada. Fora desses casos, descobertas locais deverão ajustar apenas o próximo passo local, sem reabrir continuamente todo o planejamento.

## Marco 1 — Núcleo mecânico do compromisso narrativo

### Objetivo

Transformar o modelo atual de compromisso narrativo em estruturas e comportamentos observáveis, construídos e testados uma unidade por vez.

Este marco existe para verificar se os conceitos atualmente descritos conseguem formar um módulo coerente antes que regras de D&D, persistência, interfaces ou IA sejam introduzidas.

### Comportamentos atualmente conhecidos

O marco deverá investigar e, quando confirmados pelo desenho emergente, proteger os seguintes comportamentos:

- uma Avaliação de Elegibilidade é determinística;
- repetir a avaliação sobre a mesma entrada produz o mesmo resultado;
- uma Avaliação de Elegibilidade não cria uma Preparação Narrativa;
- elementos rígidos de uma Preparação não podem ser adaptados discricionariamente;
- uma Avaliação de Materialização não altera o Cânone da História;
- repetir a mesma solicitação de Materialização não cria duas Situações;
- uma Preparação Narrativa pertence a uma única Intenção Narrativa;
- uma Situação pode materializar Preparações compatíveis de Intenções Narrativas diferentes.

Essa lista descreve o destino conhecido do marco, não uma ordem de implementação nem uma decisão antecipada sobre classes, métodos ou arquivos.

### Estados e transições

O marco também deverá tornar visíveis os estados e as transições exigidos pelos cenários compreendidos. Enums, objetos de estado e outros formatos permanecem alternativas a serem avaliadas quando surgir a primeira necessidade concreta.

Não se pretende provar que uma representação cobre toda campanha possível. A evidência procurada é que ela cubra os cenários conhecidos e não permita que estados intermediários ou transições ainda não compreendidas ocorram silenciosamente.

Um caso que pareça ficar "entre dois estados" deverá ser examinado para descobrir se revela:

- um estado ausente;
- duas dimensões indevidamente comprimidas;
- uma transição ainda não representada;
- uma condição temporária que não deveria ser estado;
- ou uma responsabilidade atribuída ao conceito errado.

### Limites deste marco

Este marco não requer:

- integração com IA;
- regras de D&D;
- banco de dados;
- formato definitivo de campanha;
- CLI ou servidor MCP;
- representação completa de todos os termos do vocabulário.

### Evidência de conclusão

O marco poderá ser considerado atingido quando os comportamentos selecionados tiverem representações compreendidas, testes locais significativos e, quando houver dois componentes capazes de colaborar, testes que demonstrem suas relações relevantes.

A revisão do marco deverá identificar conceitos confirmados, conceitos alterados, abstrações desnecessárias e lacunas que afetem o próximo marco.

## Marco 2 — Corpo mínimo das regras de D&D

### Objetivo

Descobrir uma estrutura determinística para a parte das regras de D&D 5.5e necessária aos primeiros fluxos de campanha.

Espera-se que esse trabalho revele pressões relacionadas a personagens, atributos, testes, recursos, tempo e consequências mecânicas. A forma exata desses conceitos não está estabelecida pelo roadmap.

O objetivo anterior à beta não é implementar todo o sistema de D&D. É formar um recorte pequeno, coerente e verificável que possa ser aplicado a uma Situação produzida pelo núcleo narrativo.

### Evidência de conclusão

Além dos testes das regras selecionadas, deverá existir ao menos uma interação comprovada entre o núcleo narrativo e o recorte de regras. Dois módulos isoladamente corretos não serão evidência suficiente de que narrativa e regras conseguem compor o mesmo fluxo.

Uma capacidade de D&D ainda ausente deverá aparecer como limitação explícita. Ela não deverá ser resolvida silenciosamente pelo Narrador durante os futuros experimentos, pois isso produziria uma validação falsa do Tessitura.

## Marco 3 — Contrato de acesso progressivo do Narrador

### Objetivo

Definir como um Narrador consulta informações e solicita comportamentos sem conhecer detalhes internos de armazenamento.

A experiência anterior sugere um hot path pequeno e níveis de acesso progressivamente mais completos, provisoriamente chamados de L1, L2, L3, L4 e L5. A quantidade de níveis, seus nomes e seus conteúdos deverão emergir das necessidades reais.

O contrato deverá preservar, quando a evidência confirmar sua utilidade:

- seleção determinística de contexto;
- separação entre estado vivo e histórico;
- fontes canônicas inequívocas;
- aprofundamento sob demanda;
- respostas compactas e versionadas;
- acesso apenas à informação pertinente ao pedido atual.

CLI, MCP e API permanecem possíveis adaptadores. O contrato não deverá ser desenhado como se um deles fosse o próprio caso de uso.

Cache interno poderá otimizar consultas do Tessitura. Cache de prompt pertence ao ambiente do modelo e não será requisito para correção ou eficiência semântica. O sistema deverá fornecer pouco contexto, corretamente escolhido, mesmo quando nenhum cache do provedor estiver disponível.

## Marco 4 — Formato portátil de campanha

### Objetivo

Definir como o Cânone da História, o Estado do Mundo, personagens, regras aplicáveis, material narrativo e registros de interação são preservados fora do código-fonte do Tessitura.

O formato deverá pertencer ao Tessitura, não ao Codex, Claude, Gemini ou outro Narrador. Sua disposição concreta em arquivos ou banco deverá responder aos padrões de leitura, escrita, versionamento e auditoria descobertos nos marcos anteriores.

A campanha deverá poder ser criada, transportada, atualizada e submetida a verificação sem exigir alterações no programa instalado.

## Marco 5 — Autoria de uma campanha experimental

### Objetivo

Tornar possível construir uma campanha pequena que exercite o recorte narrativo e mecânico já existente.

Deverão ser investigadas formas de iniciar uma campanha por conversa guiada, preenchimento assistido, importação ou uso de um pacote pronto. Também deverá ser considerada a diferença entre coautoria, na qual o Jogador conhece e decide mais elementos, e jogo com surpresa, no qual o Narrador preserva informações que o personagem desconhece.

Um guia de criação de campanha deverá registrar apenas o processo que tiver sido compreendido e exercitado. Ele não deverá antecipar uma metodologia universal de autoria.

A campanha experimental deverá possuir verdade conhecida e limites claros o bastante para permitir comparação posterior entre o que ocorreu e o que poderia legitimamente ocorrer.

## Marco 6 — Primeiros adaptadores de integração

### Objetivo

Permitir que pessoas e Narradores utilizem os mesmos casos de uso sem acessar diretamente a implementação ou interpretar livremente os arquivos internos da campanha.

A CLI permanece candidata natural para operação humana, autoria, diagnóstico e compatibilidade com o modo baseado em repositório. Um servidor MCP local é o principal candidato atual para oferecer ferramentas e contexto a diferentes agentes. Essas escolhas deverão ser confirmadas pela pressão observada quando o marco se aproximar.

O modo "repositório + agente" poderá permanecer como baseline técnico. O modo portátil deverá separar programa e campanha e evitar que o Narrador precise vasculhar o código-fonte.

Instruções ou pacotes específicos para um fornecedor poderão existir como adaptações externas. Eles não deverão alterar o formato canônico da campanha nem introduzir regras de negócio exclusivas daquele fornecedor.

## Marco 7 — Primeiro experimento integrado com IA

### Objetivo

Verificar se uma IA Narradora consegue criar e conduzir uma campanha pequena usando o Tessitura para contexto, regras e alteração controlada do estado.

Antes das execuções, deverão ser escolhidas as perguntas do experimento, os comportamentos esperados e os critérios de avaliação. Resultados mecânicos deverão ser distinguidos de julgamentos qualitativos sobre coerência, ritmo, adequação narrativa e respeito à agência do Jogador.

Os rollouts dos clientes poderão ser preservados como evidência bruta. A avaliação deverá depender de um registro normalizado controlado pelo Tessitura, capaz de relacionar pelo menos:

- estado inicial relevante;
- informação apresentada ao Narrador;
- declaração do Jogador;
- operações solicitadas;
- resultados produzidos pelo Tessitura;
- decisões e justificativas do Narrador;
- resposta apresentada ao Jogador;
- alterações canônicas resultantes;
- resultado esperado ou conjunto de resultados aceitáveis.

O mesmo núcleo e a mesma campanha deverão, quando praticável, ser exercitados por mais de uma forma de acesso. Isso ajudará a distinguir problemas do Tessitura de comportamentos particulares de um Narrador ou cliente.

## Marco 8 — Primeira publicação beta

### Objetivo

Disponibilizar uma versão pequena e explicitamente experimental para observar instalação, criação de campanha, jogo e integração fora do ambiente de desenvolvimento original.

A hipótese atual para a beta inclui duas experiências comparáveis:

1. um modo de referência baseado em repositório e agente, destinado a desenvolvimento, reprodução e usuários técnicos;
2. um modo local portátil, no qual Tessitura e campanha são instalados ou criados separadamente e um Narrador utiliza o contrato exposto pela aplicação.

O servidor MCP local é o candidato prioritário para o segundo modo, mas essa escolha ainda dependerá das evidências dos marcos anteriores. A beta deverá procurar exercitar ao menos um ambiente diferente do baseline original "repositório + Codex".

Próximo da publicação deverão ser decididos, com base no produto que efetivamente existir:

- sistemas operacionais inicialmente suportados;
- formato dos artefatos de instalação;
- mecanismo de atualização e migração de campanhas;
- instruções de instalação e desinstalação;
- campanha ou cenário de exemplo;
- diagnósticos necessários para relatos de erro;
- forma de coletar feedback sem presumir telemetria automática;
- limitações conhecidas que precisarão ser comunicadas.

### Perguntas da beta

A primeira publicação deverá ajudar a responder, entre outras perguntas que emerjam:

- uma pessoa consegue instalar ou iniciar o Tessitura seguindo a documentação?
- ela consegue criar, importar ou abrir uma campanha?
- o Narrador encontra o contexto necessário sem receber o Cânone inteiro?
- narrativa e regras determinísticas colaboram no mesmo fluxo?
- a campanha permanece coerente durante várias Interações?
- os registros produzidos permitem reconstruir e avaliar o que aconteceu?
- a mesma campanha pode ser utilizada fora do modo "repositório + Codex"?
- problemas observados pertencem ao núcleo, ao adaptador, ao conteúdo ou ao Narrador?

## Fora do compromisso da primeira beta

Este roadmap não compromete a primeira beta com:

- implementação completa de todas as regras de D&D 5.5e;
- suporte equivalente a todos os agentes e fornecedores de IA;
- aplicação gráfica própria com Narrador embutido;
- serviço hospedado de campanhas ou MCP remoto;
- publicação em marketplaces de agentes;
- metodologia definitiva para criar qualquer tipo de campanha;
- garantia de economia baseada em cache de prompt;
- estabilidade de produção, compatibilidade retroativa irrestrita ou disponibilidade contínua.

Essas possibilidades permanecem direções posteriores. A beta existe para produzir a evidência necessária para decidir quais delas merecem entrar em um roadmap futuro.
