"""Módulo de acordes.

O módulo de acordes conta com funções e ferramentas necessárias para a geração
de acordes.
"""

from notas_musicais.escalas import NOTAS, escala


def _menor(cifra):
    nota, _ = cifra.split('m')

    if '+' in cifra:
        tonica, terca, quinta = triade(nota, 'menor')
        notas = [tonica, terca, semitom(quinta, +1)]
        graus = ['I', 'III-', 'V+']
    else:
        notas = triade(nota, 'menor')
        graus = ['I', 'III-', 'V']

    return notas, graus


def semitom(nota: str, intervalo: int) -> str:
    """Calcula a distância em semitons para uma outra nota usando intervalos.

    Parameters:
        nota: Uma nota qualquer.
        intervalo: Um intervalo em semitons.

    Returns:
        Uma nota correspondente ao intervalo.

    Examples:
        >>> semitom('C', +1)
        'C#'

        >>> semitom('c', -1)
        'B'
    """
    pos = NOTAS.index(nota.upper()) + intervalo

    return NOTAS[pos % 12]


def triade(nota: str, tonalidade: str) -> list[str]:
    """Gera tríades a partir de uma tônica e uma tonalidade.

    Parameters:
        nota: Uma nota da qual se deseja obter um acorde.
        tonalidade: Tonalidade na qual será formado o acorde.

    Returns:
        Uma lista contendo a tríade do acorde referente a nota na tonalidade
        desejada.

    Examples:
        >>> triade('C', 'maior')
        ['C', 'E', 'G']

        >>> triade('C', 'menor')
        ['C', 'D#', 'G']
    """
    graus = (0, 2, 4)
    notas_escala = escala(nota, tonalidade)['notas']

    return [notas_escala[grau] for grau in graus]


def acorde(cifra: str) -> dict[str, list[str]]:
    """Gera as notas de um acorde (tríade) a partir de uma cifra.

    Parameters:
        cifra: Um acorde em forma de cifra.

    Returns:
        Um dicionário com as notas e os graus correspondentes à escala maior.

    Examples:
        >>> acorde('C')
        {'notas': ['C', 'E', 'G'], 'graus': ['I', 'III', 'V']}

        >>> acorde('Cm')
        {'notas': ['C', 'D#', 'G'], 'graus': ['I', 'III-', 'V']}

        >>> acorde('Co')
        {'notas': ['C', 'D#', 'F#'], 'graus': ['I', 'III-', 'V-']}

        >>> acorde('C+')
        {'notas': ['C', 'E', 'G#'], 'graus': ['I', 'III', 'V+']}

        >>> acorde('Cm+')
        {'notas': ['C', 'D#', 'G#'], 'graus': ['I', 'III-', 'V+']}
    """
    if 'm' in cifra:
        notas, graus = _menor(cifra)

    elif 'o' in cifra:
        nota, _ = cifra.split('o')
        tonica, terca, quinta = triade(nota, 'menor')
        notas = [tonica, terca, semitom(quinta, -1)]
        graus = ['I', 'III-', 'V-']

    elif '+' in cifra:
        nota, _ = cifra.split('+')
        tonica, terca, quinta = triade(nota, 'maior')
        notas = [tonica, terca, semitom(quinta, +1)]
        graus = ['I', 'III', 'V+']

    else:
        notas = triade(cifra, 'maior')
        graus = ['I', 'III', 'V']

    return {'notas': notas, 'graus': graus}
