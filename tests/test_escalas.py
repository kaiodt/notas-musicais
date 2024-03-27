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
    ('tonica', 'esperado'),
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
    ],
)
def test_deve_retornar_notas_corretas(tonica, esperado):
    assert escala(tonica, 'maior')['notas'] == esperado


def test_deve_retornar_os_sete_graus():
    graus = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    assert escala('C', 'maior')['graus'] == graus
