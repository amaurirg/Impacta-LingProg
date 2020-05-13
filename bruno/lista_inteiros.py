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

entrada = input("Digite números inteiros separados por um espaço e pressione ENTER: ").split(' ')
lista_inteiros = entrada

while True:
    entrada = input("Digite o comando que deseja seguido de números inteiros\n"
                    "separados por um espaço e pressione ENTER: ").split(' ')

    if entrada[0] == "inserir":
        lista_inteiros += entrada[1:]

    elif entrada[0] == "remover":
        lista_inteiros.remove(entrada[1])

    elif entrada[0] == "parcial":
        print(lista_inteiros, sep=' ')

    elif entrada[0] == "final":
        print(lista_inteiros, sep=' ')
        exit(0)
