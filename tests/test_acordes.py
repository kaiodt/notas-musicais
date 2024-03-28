import pytest

from notas_musicais.acordes import acorde


@pytest.mark.parametrize(
    ('cifra', 'esperado'),
    [
        ('C', ['C', 'E', 'G']),
        ('F#', ['F#', 'A#', 'C#']),
        ('Cm', ['C', 'D#', 'G']),
        ('Co', ['C', 'D#', 'F#']),
        ('C+', ['C', 'E', 'G#']),
        ('Cm+', ['C', 'D#', 'G#']),
    ],
)
def test_acorde_deve_retornar_notas_correspondentes(cifra, esperado):
    assert acorde(cifra)['notas'] == esperado


@pytest.mark.parametrize(
    ('cifra', 'esperado'),
    [
        ('C', ['I', 'III', 'V']),
        ('Cm', ['I', 'III-', 'V']),
        ('Co', ['I', 'III-', 'V-']),
        ('C+', ['I', 'III', 'V+']),
        ('Cm+', ['I', 'III-', 'V+']),
    ],
)
def test_acorde_deve_retornar_graus_correspondentes(cifra, esperado):
    assert acorde(cifra)['graus'] == esperado
