'''O objetivo desse problema é a implementação de funções que indiquem se um determinado ano é ou não bissexto.

Para cada ano fornecido ao programa, faz-se necessário, primeiro, identificar se o ano fornecido é um valor inteiro de 4 dígitos e,
segundo, dado que o ano é um número válido, informar se é ou não um ano bissexto.

Um ano é bissexto se ele satisfaz as seguintes condições:

É divisível por 4 e,
Não é divisível por 100 ou é divisível por 400.
A sua tarefa é construir uma solução com três funções (3): contaDigitos, ehBissexto e Mensagem.

Formato de entrada

A entrada consiste numa lista de valores separados por um espaço em branco.

Para cada valor da entrada uma mensagem deve ser exibida.

Se o valor é um ano bissexto mas for um ano anterior ao ano atual: O ano xxxx foi bissexto
Se o valor é um ano bissexto mas for um ano posterior ao ano atual: O ano xxxx serah bissexto
Se o valor não é um ano bissexto: O ano xxxx NAO eh bissexto
Se o número não é um ano de 4 dígitos: Ano invalido
'''
from datetime import datetime

def contaDigitos(ano):
    return len(ano)

def ehBissexto(ano):
    ano = int(ano)
    ano_atual = datetime.now().year
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        if ano < ano_atual:
            return 'Foi Bissexto'
        else:
            return 'Será Bissexto'            

def Mensagem(ano):
    if contaDigitos(ano) < 4:
        return 'Ano invalido'
    elif ehBissexto(ano) == 'Foi Bissexto':
        return 'O ano {} foi bissexto'.format(ano)
    elif ehBissexto(ano) == 'Será Bissexto':
        return 'O ano {} serah bissexto'.format(ano)
    else:
        return 'O ano {} NAO eh bissexto'.format(ano)

lista = input().split()

for ano in lista:
    print(Mensagem(ano))
