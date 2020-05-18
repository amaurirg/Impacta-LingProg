from agenda import Telefone


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


def test_valida_telefone_valido():
    try:
        tel1 = Telefone("123456789")
        tel2 = Telefone("11-2345-6789")
    except ValueError:
        pass
    else:
        assert tel1.telefone == "123456789"
        assert tel2.telefone == "11-2345-6789"
        assert tel1.valida_telefone(tel1.telefone) == True
        assert tel1.valida_telefone(tel2.telefone) == True
        assert tel1._numero_de_digitos == 9
        assert tel2._numero_de_digitos == 10


def test_valida_telefone_invalido_1():
    try:
        Telefone(1123456789)
    except TypeError:
        pass
    else:
        raise AssertionError('Telefone deve ser do tipo string')


def test_valida_telefone_invalido_2():
    try:
        Telefone(("não é número"))
        Telefone("12345678901092")
        Telefone("901092")
    except ValueError:
        pass
    else:
        raise AssertionError('Telefone pode conter hífens e ter de 8 a 11 dígitos')


def test_digitos():
    tel2 = Telefone("11-2345-6789")
    assert tel2.digitos(tel2.telefone) == "1123456789"


def test_eh_celular():
    tel1 = Telefone("999999999")
    tel2 = Telefone("11999999999")
    assert tel1.eh_celular == True
    assert tel2.eh_celular == True


def test_eh_fixo():
    tel1 = Telefone("22222222")
    tel2 = Telefone("1122222222")
    assert tel1.eh_fixo == True
    assert tel2.eh_fixo == True


def test_possui_ddd():
    tel1 = Telefone("22222222")
    tel2 = Telefone("1122222222")
    assert tel1.possui_ddd == False
    assert tel2.possui_ddd == True


def test_to_json():
    tel1 = Telefone("123456789")
    tel2 = Telefone("11-2345-6789")
    assert tel1.to_json() == "123456789"
    assert tel2.to_json()== "11-2345-6789"


def test__repr__():
    tel = Telefone("123456789")
    assert tel.__repr__() == '<Telefone: 123456789>'
