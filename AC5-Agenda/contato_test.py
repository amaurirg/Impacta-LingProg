from agenda import Contato, CreateContactError


def test_cria_contato():
    try:
        c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    except TypeError:
        assert False, "Erro ao criar o contato"
    else:
        assert c.nome == "Aluno"
        assert c.telefone == "1199999-9999"
        assert c.email == "aluno@aluno.faculdadeimpacta.com.br"


def test_nao_cria_contato():
    try:
        c = Contato(123, "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
        c = Contato('', "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    except TypeError:
        assert True, "Erro ao criar o contato"
    except Exception:
        assert CreateContactError() == "O nome não foi informado!"

