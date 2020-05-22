from agenda import Agenda, Contato


def test_instancia():
    a = Agenda("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    assert isinstance(a, Agenda) is True


def test_novo_contato_invalido():
    lista = [{'nome': 'Aluno', 'telefone': 11999999999, 'email': 'aluno@aluno.faculdadeimpacta.com.br'},
             {'nome': 'Aluno', 'telefone': '1199999-9999', 'email': 123},
             {'nome': 'Aluno', 'telefone': '1199999-9999', 'email': 'alunoaluno.faculdadeimpacta.com.br'}]
    for i in lista:
        try:
            a = Agenda(i['nome'], i['telefone'], i['email'])
        except TypeError:
            pass
        except ValueError:
            pass
        except Exception:
            AssertionError("Não levantou erro de tipo")
        else:
            assert isinstance(a, Agenda) is False


def test_novo_contato():
    # a = Agenda("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    pass
