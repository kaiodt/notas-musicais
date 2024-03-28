import re

import pytest

from notas_musicais.escalas import ESCALAS, NOTAS, escala


def test_deve_funcionar_com_notas_minusculas():
    assert escala(tonica='c', tonalidade='maior')


def test_deve_retornar_erro_quando_nota_nao_existe():
    mensagem_erro = f'Essa nota não existe. Tente uma dessas: {NOTAS}.'

    with pytest.raises(ValueError, match=re.escape(mensagem_erro)):
        escala(tonica='X', tonalidade='maior')


def test_deve_retornar_erro_quando_escala_nao_existe():
    mensagem_erro = (
        'Essa escala não existe ou não foi implementada. '
        f'Tente uma dessas: {list(ESCALAS.keys())}'
    )

    with pytest.raises(KeyError, match=re.escape(mensagem_erro)):
        escala(tonica='C', tonalidade='X')


@pytest.mark.parametrize(
    ('tonica', 'tonalidade', 'esperado'),
    [
        ('C', 'maior', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', 'maior', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', 'maior', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
        ('C', 'menor', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
        ('C#', 'menor', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']),
        ('F', 'menor', ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']),
    ],
)
def test_deve_retornar_notas_corretas(tonica, tonalidade, esperado):
    assert escala(tonica, tonalidade)['notas'] == esperado


def test_deve_retornar_os_sete_graus():
    graus = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    assert escala('C', 'maior')['graus'] == graus
