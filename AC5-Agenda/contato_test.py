from agenda import Contato, CreateContactError, Telefone


def test_cria_contato():
    try:
        c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    except TypeError:
        assert False, "Erro ao criar o contato"
    else:
        assert c.nome == "Aluno"
        # assert c.telefone == "1199999-9999"
        assert c.email == "aluno@aluno.faculdadeimpacta.com.br"
        # assert c.get_telefones() == {'principal': <Telefone: 1199999-9999>}


def test_nao_cria_contato():
    try:
        c = Contato(123, "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
        c = Contato('', "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
        c = Contato("Aluno", 11999999999, "aluno@aluno.faculdadeimpacta.com.br")
        c = Contato("Aluno", "1199999-9999", "aluno.faculdadeimpacta.com.br")
    except TypeError:
        assert True, "Erro ao criar o contato"
    except Exception:
        assert CreateContactError() == "O nome não foi informado!"


def test_adiciona_telefone():
    c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    c.adiciona_telefone("113322-4567", "fixo")
    c.adiciona_telefone("1198888-8888", "celular")
    assert c.telefones == {'principal': Telefone("1199999-9999"), 'fixo': Telefone("113322-4567"),
                           'celular': Telefone("1198888-8888")}
