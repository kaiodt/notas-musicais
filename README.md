<p align="center">
  <img src="https://notas-musicais-kaiodtr.readthedocs.io/pt-br/latest/assets/logo.png" width="200">
</p>

# Notas Musicais

[![CI](https://github.com/kaiodt/notas-musicais/actions/workflows/pipeline.yml/badge.svg)](https://github.com/kaiodt/notas-musicais/actions)
[![codecov](https://codecov.io/gh/kaiodt/notas-musicais/graph/badge.svg?token=I4ASWFMXVL)](https://codecov.io/gh/kaiodt/notas-musicais)
[![Documentation Status](https://readthedocs.org/projects/notas-musicais-kaiodtr/badge/?version=latest)](https://notas-musicais-kaiodtr.readthedocs.io/pt-br/latest/?badge=latest)

**Notas Musicais** é um CLI para ajudar na formação de escalas, acordes e campos harmônicos.

A aplicação é baseada em um comando chamado `notas-musicais`, que tem um subcomando relacionado a cada ação que a aplicação pode realizar, sendo:

- `escala`
- `acorde`
- `campo-harmonico`

## Como Instalar

Para instalação do CLI do projeto, recomendamos o uso do `pipx`:

```bash
pipx install notas-musicais
```

Isso é apenas uma recomendação. Você também pode instalar o projeto com o gerenciador de sua preferência. Por exemplo, com o `pip`:

```bash
pip install notas-musicais
```


## Como Usar

### Escalas

Você pode executar a funcionalidade de **escalas** via linha de comando.

Por exemplo, o comando:

```bash
notas-musicais escala
```

Retorna os graus e as notas correspondentes da escala de **Dó** (**C**) **maior**:

```bash
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

#### Escolhendo a Tônica da Escala

O primeiro parâmetro do CLI é a tônica da escala que você deseja exibir. Com isso, é possível alterar a escala retornada.

Por exemplo, o comando:

```bash
notas-musicais escala F#
```

Retorna os graus e as notas correspondentes da escala de **Fá sustenido** (**F#**) **maior**:

```bash
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

#### Escolhendo a Tonalidade da Escala

Também é possível alterar a tonalidade da escala que você deseja exibir. Para isso, use o segundo parâmetro do CLI.

Por exemplo, o comando:

```bash
notas-musicais escala D# menor
```

Retorna os graus e as notas correspondentes da escala de **Ré sustenido** (**D#**) **menor**:

```bash
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ D# │ F  │ F#  │ G# │ A# │ B  │ C#  │
└────┴────┴─────┴────┴────┴────┴─────┘
```

### Acordes

Você pode executar a funcionalidade de **acordes** via linha de comando.

Por exemplo, o comando:

```bash
notas-musicais acorde
```

Retorna os graus e as notas correspondentes ao acorde de **Dó** (**C**) **maior**:

```bash
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

#### Escolhendo a Cifra do Acorde

Também é possível passar como argumento para o comando a cifra do acorde desejado.

Por exemplo, o comando:

```bash
notas-musicais acorde C+
```

Retorna os graus e as notas correspondentes ao **acorde aumentado** de **Dó** (**C+**):

```bash
┏━━━┳━━━━━┳━━━━┓
┃ I ┃ III ┃ V+ ┃
┡━━━╇━━━━━╇━━━━┩
│ C │ E   │ G# │
└───┴─────┴────┘
```

Até o momento, estão disponíveis:

- Acordes maiores
- Acordes menores
- Acordes diminutos
- Acordes aumentados
- Acorder menores aumentados

### Campos Harmônicos

Você pode executar a funcionalidade de **campos harmônicos** via linha de comando.

Por exemplo, o comando:

```bash
notas-musicais campo-harmonico
```

Retorna as cifras e os graus correspondentes do campo harmônico de **Dó** (**C**) **maior**:

```bash
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━━┓
┃ I ┃ ii ┃ iii ┃ IV ┃ V ┃ vi ┃ vii° ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━━┩
│ C │ Dm │ Em  │ F  │ G │ Am │ Bo   │
└───┴────┴─────┴────┴───┴────┴──────┘
```

#### Escolhendo a Tônica do Campo Harmônico

Também é possível alterar a tônica do campo harmônico usando o primeiro parâmetro do subcomando.

Por exemplo, o comando:

```bash
notas-musicais campo-harmonico E
```

Retorna as cifras e os graus correspondentes do campo harmônico de **Mi** (**E**) **maior**:

```bash
┏━━━┳━━━━━┳━━━━━┳━━━━┳━━━┳━━━━━┳━━━━━━┓
┃ I ┃ ii  ┃ iii ┃ IV ┃ V ┃ vi  ┃ vii° ┃
┡━━━╇━━━━━╇━━━━━╇━━━━╇━━━╇━━━━━╇━━━━━━┩
│ E │ F#m │ G#m │ A  │ B │ C#m │ D#o  │
└───┴─────┴─────┴────┴───┴─────┴──────┘
```

#### Escolhendo a Tonalidade da Escala

Também é possível alterar a tonalidade do campo harmônico usando o segundo parâmetro do subcomando.

Por exemplo, o comando:

```bash
notas-musicais campo-harmonico E menor
```

Retorna os graus e as notas correspondentes da escala de **Mi** (**E**) **menor**:

```bash
┏━━━━┳━━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ i  ┃ ii° ┃ III ┃ iv ┃ v  ┃ VI ┃ VII ┃
┡━━━━╇━━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ Em │ F#o │ G   │ Am │ Bm │ C  │ D   │
└────┴─────┴─────┴────┴────┴────┴─────┘
```


## Ajuda do CLI

Para exibir as possíveis opções do CLI, use a flag `--help`.

```bash
notas-musicais --help
```

```bash
 Usage: notas-musicais [OPTIONS] COMMAND [ARGS]...

╭─ Options ──────────────────────────────────────────────────────────────╮
│ --install-completion        [bash|zsh|fish|power  Install completion   │
│                             shell|pwsh]           for the specified    │
│                                                   shell.               │
│                                                   [default: None]      │
│ --show-completion           [bash|zsh|fish|power  Show completion for  │
│                             shell|pwsh]           the specified shell, │
│                                                   to copy it or        │
│                                                   customize the        │
│                                                   installation.        │
│                                                   [default: None]      │
│ --help                                            Show this message    │
│                                                   and exit.            │ 
╰────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────╮
│ acorde                                                                 │
│ campo-harmonico                                                        │
│ escala                                                                 │
╰────────────────────────────────────────────────────────────────────────╯
```

### Informações Sobre os Subcomandos

As informaçães sobre cada subcomando podem ser acessadas usando a flag `--flag` após o nome do subcomando.

Por exemplo:

```bash
notas-musicais campo-harmonico --help
```

```bash
 Usage: notas-musicais campo-harmonico [OPTIONS] [TONICA] [TONALIDADE]

╭─ Arguments ────────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tônica do campo harmônico [default: C] │
│   tonalidade      [TONALIDADE]  Tonalidade do campo harmônico          │
│                                 [default: maior]                       │
╰────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                            │
╰────────────────────────────────────────────────────────────────────────╯
```
