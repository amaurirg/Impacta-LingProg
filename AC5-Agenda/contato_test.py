from agenda import Contato, CreateContactError, Telefone

from agenda import (Contato, CreateContactError, DeleteError,
                    Email, Telefone)


class TelefoneAtualizado(Telefone):
    """
    Eu esqueci de incluir este método na classe de Telefone, então
    estou criando esta classe para poder adicionar o método à classe Telefone
    sem que vocês precisem editar o código de vocês. Basta usar a nova classe
    que criei durantes os testes, como fiz.

    Portanto NÃO INCLUAM este método na classe Telefone de vocês.
    """

    def __eq__(self, other):
        if not isinstance(other, Telefone):
            raise TypeError('Não é possível comparar um Telefone com '
                            'objetos de outro tipo')
        n_self = self.telefone.replace('-', '')
        n_other = other.telefone.replace('-', '')
        return n_self == n_other


def test_cria_contato():
    try:
        c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    except TypeError:
        assert False, "Erro ao criar o contato"
    else:
        assert c.nome == "Aluno"
        assert c.get_telefones()['principal'] == TelefoneAtualizado("1199999-9999")
        assert c.get_emails()['principal'] == Email("aluno@aluno.faculdadeimpacta.com.br")


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
    assert c.get_telefones()['principal'] == TelefoneAtualizado("1199999-9999")
    assert c.get_telefones()['fixo'] == TelefoneAtualizado("113322-4567")
    assert c.get_telefones()['celular'] == TelefoneAtualizado("1198888-8888")


def test_adiciona_telefone_invalido_1():
    c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    try:
        # c.adiciona_telefone("11332211-456789", "fixo")
        # c.adiciona_telefone("1198888", "celular")
        # c.adiciona_telefone('', "fixo")
        # c.adiciona_telefone("1199999-9999", "principal")
        c.adiciona_telefone("1198888-8888")
    except ValueError:
        pass
    # else:
    #     raise AssertionError('Telefone pode conter hífens e ter de 8 a 11 dígitos')
    assert not any(['fixo' in c.get_telefones()])
    assert c.get_telefones()['principal'] == TelefoneAtualizado("1199999-9999")
    # assert c.get_telefones()['principal'] == TelefoneAtualizado("1198888-8888")


def test_adiciona_telefone_invalido_2():
    c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    try:
        c.adiciona_telefone(1198888, "celular")
        c.adiciona_telefone(11.98888-8888, "celular")
    except TypeError:
        pass
    else:
        raise AssertionError('Telefone deve ser do tipo string')
    assert not any(['celular' in c.get_telefones()])


def test_adiciona_email():
    c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    c.adiciona_email("aluno@gmail.com", "particular")
    c.adiciona_email("aluno@outrodominio.com.br", "extra")
    assert c.get_emails()['principal'] == Email('aluno@aluno.faculdadeimpacta.com.br')
    assert c.get_emails()['particular'] == Email('aluno@gmail.com')
    assert c.get_emails()['extra'] == Email('aluno@outrodominio.com.br')
