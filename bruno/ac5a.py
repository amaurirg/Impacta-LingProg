numero = int(input())
soma = 0

while numero != 0:
    resto = numero % 10
    numero //= 10
    soma +=resto
    
print(soma)
