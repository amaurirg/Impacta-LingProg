import os

from agenda import Agenda, Contato, Telefone


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
    assert len(a.busca_contatos('uno1')) == 1
    assert len(a.busca_contatos('@')) == 3


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

    assert a.ligar('11511') == f'Ligando para Aluno1: {Telefone("115111-1111")}'
    assert a.ligar('11') == f'Ligando para Aluno1: {Telefone("115111-1111")}'
    assert a.ligar('faculdade') == f'Ligando para Aluno1: {Telefone("115111-1111")}'
    # assert a.ligar('faculdade', "celular") == f'Ligando para Aluno2: {Telefone("115222-2222")}'
    # assert a.ligar('faculdade') == f'Ligando para Aluno1: {Telefone("115111-1111")}'
    # assert a.ligar('faculdade') == f'Ligando para Aluno1: {Telefone("115111-1111")}'
    # assert a.ligar('faculdade') == f'Ligando para Aluno1: {Telefone("115111-1111")}'


def test_apagar_contato():
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
    assert len(a.contatos) == 3
    a.apagar_contato("aluno1@aluno.faculdadeimpacta.com.br")
    a.apagar_contato('333@')
    a.apagar_contato('uno')
    assert len(a.contatos) == 1
    assert a.contatos[0].nome == 'Aluno3'


def test_exportar_contatos():
    a = Agenda("Dono da Agenda", "1198765-4321", "dono@faculdadeimpacta.com.br")
    a.novo_contato("Aluno1", "115111-1111", "aluno1@aluno.faculdadeimpacta.com.br")
    a.novo_contato("Aluno2", "115222-2222", "aluno2@aluno.faculdadeimpacta.com.br")
    a.novo_contato("Aluno3", "115333-3333", "aluno3@aluno.faculdadeimpacta.com.br")
    a.novo_contato('Ana', '11999888563', 'ana@email.com')
    a.novo_contato('Pedro', '1955552222', 'pedro@email.com')
    a.novo_contato('Mariana', '21145145145', 'mariana@email.com')
    a.novo_contato('João', '1152525252', 'joao@email.com')
    a.exportar_contatos('contatos.json')
    assert True, os.path.exists('contatos.json')
    assert True, os.path.isfile('contatos.json')


def test_carregar_contatos():
    a = Agenda("Dono da Agenda", "1198765-4321", "dono@faculdadeimpacta.com.br")
    assert a.carregar_contatos('contatos.json') == [
        {
            "nome": "Aluno1",
            "telefones": {
                "principal": "115111-1111"
            },
            "emails": {
                "principal": "aluno1@aluno.faculdadeimpacta.com.br"
            }
        },
        {
            "nome": "Aluno2",
            "telefones": {
                "principal": "115222-2222"
            },
            "emails": {
                "principal": "aluno2@aluno.faculdadeimpacta.com.br"
            }
        },
        {
            "nome": "Aluno3",
            "telefones": {
                "principal": "115333-3333"
            },
            "emails": {
                "principal": "aluno3@aluno.faculdadeimpacta.com.br"
            }
        },
        {
            "nome": "Ana",
            "telefones": {
                "principal": "11999888563"
            },
            "emails": {
                "principal": "ana@email.com"
            }
        },
        {
            "nome": "Pedro",
            "telefones": {
                "principal": "1955552222"
            },
            "emails": {
                "principal": "pedro@email.com"
            }
        },
        {
            "nome": "Mariana",
            "telefones": {
                "principal": "21145145145"
            },
            "emails": {
                "principal": "mariana@email.com"
            }
        },
        {
            "nome": "João",
            "telefones": {
                "principal": "1152525252"
            },
            "emails": {
                "principal": "joao@email.com"
            }
        }
    ]
