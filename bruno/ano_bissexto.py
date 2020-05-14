"""
A cada quatro anos, o mês de fevereiro tem 29 dias, em vez de 28, como ocorre nos três anos anteriores.
Por que isso acontece? A resposta é um misto de aula de matemática e de história.
O ano é o tempo que demora para a Terra dar uma volta em torno do Sol: 365 dias e aproximadamente seis horas.
Mas, como você pode perceber, no calendário os anos têm 365 dias exatos (e não 365 dias e 6 horas!).
Essas horas são acumuladas e, a cada quatro anos, acumulam 24 horas - isto é, um dia!
Sem esse ajuste, o calendário iria ficando, com o passar dos anos, defasado - e o dia em que se comemora o início
da primavera, por exemplo, poderia passar a não coincidir com o evento comemorado.

Como calcular um ano bissexto

Se o ano não termina em 00, ele é bissexto caso seja divisível por 4. Exemplos: 1988, 1992, 1996, e assim por diante.

Nota: Um número é divisível por 4 se a sua dezena (1988 = 88) é divisível por 4.

Como o tempo que a Terra leva para dar a volta em torno do Sol é estimado em
aproximadamente 365 dias, 5 horas, 48 minutos e 46 segundos, essa pequena diferença de menos de 12 minutos poderia
provocar erros a cada cerca de 120 anos.

Logo, a regra para os anos terminados em 00 é:

O ano terminado em 00 será bissexto se for divisível por 400. Veja a tabela:

1500	Não bissexto
1600	Bissexto
1700	Não bissexto
1800	Não bissexto
1900	Não bissexto
2000	Bissexto
2100	Não bissexto

Essa diferença de 46 segundos pode provocar novas revisões no calendário. Mas a revisão só ocorrerá depois do ano 3000.
Os astrônomos têm corrigido os relógios mundiais em 1 segundo em algumas passagens de ano, o que poderá dispensar
tal revisão.

Essas correções são necessárias, por exemplo, nos sistemas de posicionamento global (GPS), em relógios atômicos, etc.

Carlos Alberto Campagner, Especial para a Página 3 Pedagogia & Comunicação é engenheiro mecânico, com mestrado
em mecânica, professor de pós-graduação e consultor de informática.
"""

def ano(number):
    resp = 'ERRO'
    if (str(number).endswith('0') and number % 400 != 0) or number % 4 != 0:
        resp = 'não é'
    else:
        resp = 'é'
    # print(resp)
    return "O ano {0} {1} bissexto".format(number, resp)


print(ano(2000))
print(ano(2100))
print(ano(1500))
print(ano(1600))
print(ano(1988))
print(ano(3))
print(ano(4))
print(ano(1997))


"""
TESTES:

assert ano(2000) == 'O ano 2000 é bissexto'
assert ano(2100) == 'O ano 2100 não é bissexto'
assert ano(1500) == 'O ano 1500 não é bissexto'
assert ano(1600) == 'O ano 1600 é bissexto'
assert ano(1988) == 'O ano 1988 é bissexto'
assert ano(3) =='O ano 3 não é bissexto'
assert ano(4) == 'O ano 4 é bissexto'
assert ano(1997) == 'O ano 1997 não é bissexto'

"""