![logo_projeto](assets/logo.png){.center width="300"}

# Notas Musicais

## Como Usar

Você pode executar a funcionalidade de **escalas** via linha de comando.

Por exemplo, o comando:

```bash
escalas
```

Retorna os graus e as notas correspondentes da escala de **Dó** (**C**) **maior**:

```bash
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

### Escolhendo a Tônica da Escala

O primeiro parâmetro do CLI é a tônica da escala que você deseja exibir. Com isso, é possível alterar a escala retornada.

Por exemplo, o comando:

```bash
escalas F#
```

Retorna os graus e as notas correspondentes da escala de **Fá sustenido** (**F#**) **maior**:

```bash
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘
```


### Escolhendo a Tonalidade da Escala

Também é possível alterar a tonalidade da escala que você deseja exibir. Para isso, use o segundo parâmetro do CLI.

Por exemplo, o comando:

```bash
escalas D# maior
```

Retorna os graus e as notas correspondentes da escala de **Ré sustenido** (**D#**) **maior**:

```bash
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ D# │ F  │ G   │ G# │ A# │ C  │ D   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

### Ajuda do CLI

Para exibir as possíveis opções do CLI, use a flag `--help`.

```bash
escalas --help
```

```bash
 Usage: cli.py [OPTIONS] [TONICA] [TONALIDADE]

╭─ Arguments ──────────────────────────────────────────────╮
│   tonica          [TONICA]      Tônica da escala         │
│                                 [default: C]             │
│   tonalidade      [TONALIDADE]  Tonalidade da escala     │
│                                 [default: maior]         │
╰──────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────╮
│ --help          Show this message and exit.              │
╰──────────────────────────────────────────────────────────╯
```