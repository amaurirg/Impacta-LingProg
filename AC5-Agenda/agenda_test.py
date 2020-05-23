from agenda import Agenda, Contato


def test_novo_contato():
    a = Agenda("Dono da Agenda", "1198765-4321", "dono@faculdadeimpacta.com.br")
    nc1 = ("Aluno1", "115111-1111", "aluno1@aluno.faculdadeimpacta.com.br")
    nc2 = ("Aluno2", "115222-2222", "aluno2@aluno.faculdadeimpacta.com.br")
    nc3 = ("Aluno3", "115333-3333", "aluno3@aluno.faculdadeimpacta.com.br")
    for nc in [nc1, nc2, nc3]:
        a.novo_contato(nc[0], nc[1], nc[2])
    assert all([a.contatos for n in [nc1, nc2, nc3]])


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


def test_busca_contatos():
    a = Agenda("Dono da Agenda", "1198765-4321", "dono@faculdadeimpacta.com.br")
    a.novo_contato("Aluno1", "115111-1111", "aluno1@aluno.faculdadeimpacta.com.br")
    a.novo_contato("Aluno2", "115222-2222", "aluno2@aluno.faculdadeimpacta.com.br")
    a.novo_contato("Aluno3", "115333-3333", "aluno3@aluno.faculdadeimpacta.com.br")
    assert a.busca_contatos('ono') == []
    assert a.busca_contatos('9876') == []
    assert a.busca_contatos('dono@') == []
    assert a.busca_contatos('yutgyughy') == []
    assert a.busca_contatos('uno1') == [
        Contato("Aluno1", "115111-1111", "aluno1@aluno.faculdadeimpacta.com.br")]
    # assert a.busca_contatos('@') == [
    #     Contato("Aluno1", "115111-1111", "aluno1@aluno.faculdadeimpacta.com.br"),
    #     Contato("Aluno2", "115222-2222", "aluno2@aluno.faculdadeimpacta.com.br"),
    #     Contato("Aluno3", "115333-3333", "aluno3@aluno.faculdadeimpacta.com.br")]


def test_ligar():
    a = Agenda("Dono da Agenda", "1198765-4321", "dono@faculdadeimpacta.com.br")
    a.novo_contato("Aluno1", "115111-1111", "aluno1@aluno.faculdadeimpacta.com.br")
    a.novo_contato("Aluno2", "115222-2222", "aluno2@aluno.faculdadeimpacta.com.br")
    a.novo_contato("Aluno3", "115333-3333", "aluno3@aluno.faculdadeimpacta.com.br")
    a.meu_contato.adiciona_telefone("112222-2222", "fixo")
    a.meu_contato.adiciona_telefone("113333-3333", "celular")
    a.meu_contato.adiciona_telefone("114444-4444", "trabalho")
    c1 = Contato("Aluno1", "115111-1111", "aluno1@aluno.faculdadeimpacta.com.br")
    c1.adiciona_telefone("111111-1111", "fixo")
    c1.adiciona_telefone("1191111-1111", "celular")
    c1.adiciona_email("aluno11@aluno.faculdadeimpacta.com.br", "email2")
    c1.adiciona_email("aluno111@aluno.faculdadeimpacta.com.br", "email3")
    c2 = Contato("Aluno2", "115222-2222", "aluno2@aluno.faculdadeimpacta.com.br")
    c2.adiciona_telefone("112222-2222", "fixo")
    c2.adiciona_telefone("1192222-2222", "celular")
    c2.adiciona_email("aluno22@aluno.faculdadeimpacta.com.br", "email2")
    c2.adiciona_email("aluno222@aluno.faculdadeimpacta.com.br", "email3")
    c3 = Contato("Aluno3", "115333-3333", "aluno3@aluno.faculdadeimpacta.com.br")
    c3.adiciona_telefone("113333-3333", "fixo")
    c3.adiciona_telefone("1193333-3333", "celular")
    c3.adiciona_email("aluno33@aluno.faculdadeimpacta.com.br", "email2")
    c3.adiciona_email("aluno333@aluno.faculdadeimpacta.com.br", "email3")

    assert a.ligar('11511') == 'Ligando para Aluno1: <telefone>'


def test_apagar_contato():
    pass


def test_exportar_contatos():
    pass


def test_carregar_contatos():
    pass
