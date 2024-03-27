import pytest
from typer.testing import CliRunner

from notas_musicais.cli import app

runner = CliRunner()


def test_escala_cli_deve_retornar_0_ao_stdout():
    assert runner.invoke(app).exit_code == 0


@pytest.mark.parametrize('nota', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_escala_cli_deve_conter_notas_na_resposta_padrao(nota):
    assert nota in runner.invoke(app).stdout


@pytest.mark.parametrize('nota', ['F', 'G', 'A', 'A#', 'C', 'D', 'E'])
def test_escala_cli_deve_conter_notas_na_resposta_de_fa(nota):
    assert nota in runner.invoke(app, ['F']).stdout


@pytest.mark.parametrize('grau', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_escala_cli_deve_conter_todos_os_graus(grau):
    assert grau in runner.invoke(app).stdout
