from agenda import Contato, CreateContactError


def test_cria_contato():
    try:
        c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    except TypeError:
        assert False, "Erro ao criar o contato"
    else:
        assert hasattr(c, '_nome')
        assert not hasattr(c, 'telefone')
        assert not hasattr(c, 'email')
        assert c._nome == "Aluno"
        assert c._telefone == "1199999-9999"
        assert c._email == "aluno@aluno.faculdadeimpacta.com.br"


def test_nao_cria_contato():
    try:
        c = Contato(123, "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
        c = Contato('', "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    except TypeError:
        assert True, "Erro ao criar o contato"
    except Exception:
        assert CreateContactError() == "O nome não foi informado!"

