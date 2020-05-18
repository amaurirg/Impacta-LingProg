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
        assert Email.valida_email(email) == True


def test_cria_email_invalido_1():
    emails = [
        "amauriimpacta.com.br",
        "am.au-ri@gm-ai.l",
        "a@g",
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
        else:
            raise AssertionError("Não pode criar instância com e-mail inválido!")


def test_eh_aluno_impacta():
    e = Email("aluno@aluno.faculdadeimpacta.com.br")
    assert e.eh_aluno_impacta == True


def test_nao_eh_aluno_impacta():
    e = Email("aluno@aluno.faculdadequalquer.com.br")
    assert e.eh_aluno_impacta == False


def test_eh_impacta():
    e = Email("professor@faculdadeimpacta.com.br")
    assert e.eh_impacta == True


def test_nao_eh_impacta():
    e = Email("professor@outrafaculdade.com.br")
    assert e.eh_impacta == False


def test_to_json():
    e = Email("aluno@aluno.faculdadeimpacta.com.br")
    assert e.to_json() == "aluno@aluno.faculdadeimpacta.com.br"


def test__eq__():
    pass

def test__repr__():
    e = Email("aluno@aluno.faculdadeimpacta.com.br")
    assert e.__repr__() == '<Email: aluno@aluno.faculdadeimpacta.com.br>'
