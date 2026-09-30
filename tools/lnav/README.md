# Formatos do lnav

Esta pasta versiona as definições que transformam os registros JSON Lines do
Tessitura em visões compactas e consultáveis no `lnav`. Os arquivos JSONL
continuam sendo os datasets de execução; os formatos controlam somente sua
apresentação e a exposição dos campos como colunas SQL virtuais.

## Formatos disponíveis

| Formato | Dataset esperado | Conteúdo principal |
| --- | --- | --- |
| `tessitura_narrative_assessment` | `narrative-assessments.jsonl` | Assessment anterior e resultante, gatilho, duração e tokens. |
| `tessitura_narrative_preparation_creation` | `narrative-preparation-creations.jsonl` | Arquétipo, Assessment vigente, descrição proposta, duração e tokens. |

## Uso direto do repositório

Não é necessário instalar os formatos para utilizá-los durante o
desenvolvimento. A opção `-I` apresenta esta pasta ao `lnav` como um diretório
adicional de configuração:

```bash
lnav -I tools/lnav artifacts/narrative-assessments.jsonl
lnav -I tools/lnav artifacts/narrative-preparation-creations.jsonl
```

Os dois datasets podem ser abertos juntos:

```bash
lnav -I tools/lnav artifacts/narrative-assessments.jsonl \
  artifacts/narrative-preparation-creations.jsonl
```

## Instalação no perfil do usuário

Na instalação atual do `lnav`, os formatos pessoais ficam em
`~/.config/lnav/formats`. O comando `lnav -h` informa o diretório efetivamente
usado caso a configuração local seja diferente.

```bash
mkdir -p ~/.config/lnav/formats
cp -R tools/lnav/formats/tessitura_narrative_assessment \
  ~/.config/lnav/formats/
cp -R tools/lnav/formats/tessitura_narrative_preparation_creation \
  ~/.config/lnav/formats/
```

Depois da instalação, a opção `-I tools/lnav` pode ser omitida.

## Produção do dataset de Preparações

Com `OPENAI_API_KEY` já exportada, o live test de criação de Preparação pode
acrescentar uma execução ao dataset:

```bash
RUN_OPENAI_LIVE_TESTS=1 \
TESSITURA_NARRATIVE_PREPARATION_CREATION_LOG_PATH=artifacts/narrative-preparation-creations.jsonl \
poetry run pytest \
  tests/live/test_openai_narrative_preparation_creation_flow.py -s
```

O teste é ignorado explicitamente quando alguma das três variáveis exigidas
não está disponível. Cada execução bem-sucedida acrescenta uma linha ao
arquivo, preservando as anteriores.
