![logo_projeto](assets/logo.png){.center width="300"}

# Notas Musicais

**Notas Musicais** é um CLI para ajudar na formação de escalas e acordes.

Existem dois comandos disponíveis: `escala` e `acorde`.

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


## Ajuda do CLI

Para exibir as possíveis opções do CLI, use a flag `--help`.

```bash
notas-musicais --help
```

```bash
 Usage: notas-musicais [OPTIONS] COMMAND [ARGS]...

╭─ Options ────────────────────────────────────────────────────────────╮
│ --install-completion        [bash|zsh|fish|powe  Install completion  │
│                             rshell|pwsh]         for the specified   │
│                                                  shell.              │
│                                                  [default: None]     │
│ --show-completion           [bash|zsh|fish|powe  Show completion for │
│                             rshell|pwsh]         the specified       │
│                                                  shell, to copy it   │
│                                                  or customize the    │
│                                                  installation.       │
│                                                  [default: None]     │
│ --help                                           Show this message   │
│                                                  and exit.           │
╰──────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────╮
│ acorde                                                               │
│ escala                                                               │
╰──────────────────────────────────────────────────────────────────────╯
```
