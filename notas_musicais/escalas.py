NOTAS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11), 'menor': (0, 2, 3, 5, 7, 8, 10)}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """Gera uma escala a partir de uma tônica e uma tonalidade.

    Parameters:
        tonica: Nota que corresponde à tônica da escala.
        tonalidade: Tonalidade desejada da escala.

    Returns:
        Dicionário com a lista de notas da escala e os respectivos graus.

    Raises:
        ValueError: Caso `tonica` não seja uma nota válida.
        KeyError: Caso `tonalidade` não exista ou não tenha sido implementada.

    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('a', 'menor')
        {'notas': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

    """
    try:
        intervalos = ESCALAS[tonalidade]
    except KeyError:
        msg = (
            'Essa escala não existe ou não foi implementada. '
            f'Tente uma dessas: {list(ESCALAS.keys())}'
        )
        raise KeyError(msg) from None

    try:
        tonica_pos = NOTAS.index(tonica.upper())
    except ValueError:
        msg = f'Essa nota não existe. Tente uma dessas: {NOTAS}.'
        raise ValueError(msg) from None

    temp = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        temp.append(NOTAS[nota])

    return {
        'notas': temp,
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }
