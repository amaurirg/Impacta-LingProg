from agenda import Email

def test_cria_email_valido():
    emails = [
        "amauri@impacta.com.br",
        "am.au-ri@gm-ai.l.com",
        "a@gm.com",
        "amauri@facul.edu",
        "ama-uri@aluno.facul.edu",
        "ama-uri.giova-ni333@aluno.facul.uk",
        "ama-uri.giova-ni333@aluno.facul-dade.br"
    ]
    for email in emails:
        e = Email(email)
        assert isinstance(e, Email) == True
        assert e.email == email


def test_cria_email_invalido_1():
    emails = [
        '',
        "aluno 1@impacta.com.br",
        "amauri@@impacta.com.br",
        "amauri..impacta.com.br",
        "amauriimpacta.com.br",
        "amauri_giovani@impacta.com.br",
        "am.au-ri@gm-ai.l",
        "a@g",
        "a@g.com.b",
        "aluno@gmail.com.brasil",
        "a@g.com",
        "ama@uri@facul.edu",
        "ama-uri@aluno.facul.",
        "ama-uri.giova-ni333@aluno.facul",
        "ama-uri.giova-ni333@.br",
        "@amauriimpacta.com.br",
        "amauriimpacta@.com.br",
        "amauri@impacta@faculdade.com.br"
    ]
    for email in emails:
        try:
            Email(email)
        except ValueError:
            pass
        except Exception:
            raise AssertionError('Levantou um erro de tipo diferente do pedido')
        else:
            raise AssertionError('Não levantou erro para email inválido')


def test_cria_email_invalido_2():
    emails = [
        123,
        12.5,
        Email("email@email.com")
    ]
    for email in emails:
        try:
            Email(email)
        except TypeError:
            pass
        except Exception:
            raise AssertionError('Levantou um erro de tipo diferente do pedido')
        else:
            raise AssertionError("Não pode criar instância com e-mail inválido!")


def test_eh_aluno_impacta():
    e = Email("aluno@aluno.faculdadeimpacta.com.br")
    assert e.eh_aluno_impacta is True


def test_nao_eh_aluno_impacta():
    e = Email("aluno@aluno.faculdadequalquer.com.br")
    assert e.eh_aluno_impacta is False


def test_eh_impacta():
    e1 = Email("professor@faculdadeimpacta.com.br")
    e2 = Email('teste@coordenacao.faculdadeimpacta.com.br')
    e3 = Email('teste@faculdadeimpacta.com.br')
    assert all([e.eh_impacta for e in [e1, e2, e3]]), "Emails deveriam retornar True"


def test_nao_eh_impacta():
    e1 = Email('teste@aluno.faculdade.com.br')
    e2 = Email('teste@impacta.com.br')
    e3 = Email('teste@faculdadeimpacta.com')
    e4 = Email('teste@faculdadeimpacta.edu.br')
    e5 = Email('teste@qqcoisafaculdadeimpacta.com.br')
    e6 = Email("professor@outrafaculdade.com.br")
    assert not any([e.eh_impacta for e in [e1, e2, e3, e4, e5, e6]]), "Emails deveriam retornar False"


def test_to_json():
    e = Email("aluno@aluno.faculdadeimpacta.com.br")
    assert e.to_json() == "aluno@aluno.faculdadeimpacta.com.br"


def test__eq__():
    e1 = Email("aluno@aluno.faculdadeimpacta.com.br")
    e2 = Email("aluno@aluno.faculdadeimpacta.com.br")
    e1.__eq__(Email("aluno@aluno.faculdadeimpacta.com.br"))
    e2.__eq__(Email("aluno@aluno.faculdadeimpacta.com.br"))
    assert e1.email == "aluno@aluno.faculdadeimpacta.com.br"
    assert e2.email == "aluno@aluno.faculdadeimpacta.com.br"


def test__eq__2():
    e1 = Email("aluno1@aluno.faculdadeimpacta.com.br")
    e2 = Email("aluno2@aluno.faculdadeimpacta.com.br")
    assert e1.email == "aluno1@aluno.faculdadeimpacta.com.br"
    assert e2.email == "aluno2@aluno.faculdadeimpacta.com.br"


def test__repr__():
    e = Email("aluno@aluno.faculdadeimpacta.com.br")
    assert e.__repr__() == '<Email: aluno@aluno.faculdadeimpacta.com.br>'
