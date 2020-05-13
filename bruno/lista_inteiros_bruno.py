"""
Escreva um programa que permita manipular uma lista de inteiros.
Inicialmente o programa deve ler os inteiros separados por espaço
em branco e armazenar em uma lista. Dado que os valores inteiros
estão armazenados, o programa deve aceitar 4 comandos: inserir,
remover, parcial e final. O comando inserir é acompanhado na mesma
linha do valor inteiro a ser inserido na lista. Da mesma forma, o
comando remover é acompanhado do valor a ser removido da lista.
Já o comando parcial deve fazer com que os dados contidos na lista
sejam impressos na tela, separados por espaços em branco e dispostos
em ordem crescente(numérica). O mesmo deve fazer o comando final,
exceto que este encerra a execução do programa.
"""

lista = input().split(' ')
lista = [int(valor) for valor in lista]
lista = sorted(lista)
funcao = input()

def inserir(numero):
    global lista
    lista.append(numero)

def remover(numero):
    global lista
    lista.remove(numero)

def parcial():
    global lista
    print(lista)

def final():
    global lista
    print(lista)

while (funcao != 0):
    funcao = input()
    if 'inserir' in funcao:
        x,numero = funcao.split()
        numero = int(numero)
        lista.inserir(numero)
    elif 'remover' in funcao:
        x,numero = funcao.split()
        numero = int(numero)
        lista.remover(numero)
    elif 'parcial' in funcao:
        lista.parcial()
    elif 'final' in funcao:
        lista.final()
        break

class Lista:
    def inserir(self, numero):
        lista.append(numero)
