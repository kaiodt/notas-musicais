"""Módulo responsável pela criação de campos harmônicos."""

from itertools import starmap

from notas_musicais.acordes import triade
from notas_musicais.escalas import escala


def _triade_na_escala(nota: str, notas_escala: list[str]) -> str:
    """Função auxiliar para saber se as notas de um acorde estão na escala.

    Examples:
        >>> _triade_na_escala('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'C'

        >>> _triade_na_escala('D', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'Dm'

        >>> _triade_na_escala('B', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'Bo'
    """
    tonica, terca, quinta = triade(nota, 'maior')

    match terca in notas_escala, quinta in notas_escala:
        case True, True:
            return tonica
        case False, True:
            return f'{tonica}m'
        case False, False:
            return f'{tonica}o'


def _converte_graus(cifra: str, grau: str) -> str:
    """Converte o grau relativo à cifra.

    Parameters:
        cifra: Cifra de um acorde.
        grau: Grau em forma maior.

    Examples:
        >>> _converte_graus('C', 'I')
        'I'

        >>> _converte_graus('Cm', 'I')
        'i'

        >>> _converte_graus('Co', 'I')
        'i°'
    """
    if 'm' in cifra:
        return grau.lower()

    if 'o' in cifra:
        return f'{grau.lower()}°'

    return grau


def campo_harmonico(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """Gera um campo harmônico a partir de uma tônica e uma tonalidade.

    Parameters:
        tonica: Primeiro grau do campo harmônico.
        tonalidade: Tonalidade para o campo. Ex: maior, menor, etc.

    Returns:
        Um dicionário com os acordes e os graus correspondentes ao campo harmônico.

    Examples:
        >>> campo_harmonico('C', 'maior')
        {'acordes': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bo'], 'graus': ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°']}

        >>> campo_harmonico('C', 'menor')
        {'acordes': ['Cm', 'Do', 'D#', 'Fm', 'Gm', 'G#', 'A#'], 'graus': ['i', 'ii°', 'III', 'iv', 'v', 'VI', 'VII']}
    """
    notas, _graus = escala(tonica, tonalidade).values()
    acordes = [_triade_na_escala(nota, notas) for nota in notas]
    graus = list(starmap(_converte_graus, zip(acordes, _graus)))

    return {'acordes': acordes, 'graus': graus}
