entrada = input()
n, k = (int(numero) for numero in entrada.split(" "))
lista_alunos = []
k-=1
while n > 0:
    aluno = str(input())
    lista_alunos.append(aluno)
    n -= 1

lista_ordenada = sorted(lista_alunos)

print(lista_ordenada[k])
