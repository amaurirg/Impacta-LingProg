import pytest
from agenda import Contato, Agenda


@pytest.fixture
def cria_contato():
    return Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")


@pytest.fixture
def add_tel(cria_contato):
    cria_contato.adiciona_telefone("113322-4567", "fixo")
    cria_contato.adiciona_telefone("1198888-8888", "celular")
    return cria_contato


@pytest.fixture
def add_email(cria_contato):
    cria_contato.adiciona_email("aluno@gmail.com", "particular")
    cria_contato.adiciona_email("aluno@outrodominio.com.br", "extra")
    return cria_contato


@pytest.fixture
def cria_agenda_com_contatos():
    a = Agenda("Dono da Agenda", "1198765-4321", "dono@faculdadeimpacta.com.br")
    a.novo_contato("Aluno1", "115111-1111", "aluno1@aluno.faculdadeimpacta.com.br")
    a.novo_contato("Aluno2", "115222-2222", "aluno2@aluno.faculdadeimpacta.com.br")
    a.novo_contato("Aluno3", "115333-3333", "aluno3@aluno.faculdadeimpacta.com.br")
    return a
