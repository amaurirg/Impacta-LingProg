lista = input().split()
lista = [int(valor) for valor in lista]


while True:
    entrada = input().split()
        
    if entrada[0] == 'inserir':
        lista.append(int(entrada[1]))
        
        
    elif entrada[0] == 'remover':
        lista.remove(int(entrada[1]))
        
    elif entrada[0] == 'parcial':
        lista = sorted(lista)
        print(*lista, sep = " ")
        
    elif entrada[0] == 'final':
        lista = sorted(lista)
        print(*lista, sep=" ")
        exit(0)

