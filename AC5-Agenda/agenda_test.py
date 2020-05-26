import os
from agenda import Agenda, Contato, Telefone


def test_novo_contato(cria_agenda_com_contatos):
    a = cria_agenda_com_contatos
    assert len(a.contatos) == 3
    assert a.contatos[0].nome == "Aluno1"
    assert a.contatos[1].nome == "Aluno2"
    assert a.contatos[2].nome == "Aluno3"


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


def test_busca_contatos(cria_agenda_com_contatos):
    a = cria_agenda_com_contatos
    assert not any([[] for _ in ['ono', '9876', 'dono@', 'yutgyughy']])
    assert len(a.busca_contatos('uno1')) == 1
    assert len(a.busca_contatos('@')) == 3


def test_ligar(cria_agenda_com_contatos, add_tel, add_email):
    a = cria_agenda_com_contatos
    c1 = add_tel
    c1 = add_email
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
    assert a.ligar('1152') == f'Ligando para Aluno2: {Telefone("115222-2222")}'
    assert a.ligar('53') == f'Ligando para Aluno3: {Telefone("115333-3333")}'


def test_apagar_contato(cria_agenda_com_contatos):
    a = cria_agenda_com_contatos
    assert len(a.contatos) == 3
    assert a.apagar_contato("aluno1@aluno.faculdadeimpacta.com.br") == "<Contato: Aluno1> excluído com sucesso!"
    assert a.apagar_contato('uno') == "<Contato: Aluno2> excluído com sucesso!"
    assert a.apagar_contato('333@') == "Nenhum contato corresponde ao email dado."
    assert a.apagar_contato('Alu') == "Nenhum contato corresponde ao email dado."
    assert a.apagar_contato('@faculdade.impacta') == "Nenhum contato corresponde ao email dado."
    assert len(a.contatos) == 1
    assert a.contatos[0].nome == "Aluno3"

def test_exportar_contatos(cria_agenda_com_contatos):
    a = cria_agenda_com_contatos
    a.novo_contato('Ana', '11999888563', 'ana@email.com')
    a.novo_contato('Pedro', '1955552222', 'pedro@email.com')
    a.novo_contato('Mariana', '21145145145', 'mariana@email.com')
    a.novo_contato('João', '1152525252', 'joao@email.com')
    a.exportar_contatos('contatos.json')
    assert True, os.path.exists('contsssatos.json')
    assert True, os.path.isfile('conttos.json')


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
