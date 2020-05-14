produtos=[]
custos=[]
codigo = 1
while codigo != 0:
    codigo,quantidade,preco = input().split()
    codigo = int(codigo)
    quantidade = float(quantidade)
    preco = float(preco)
    custo = quantidade * preco
    produtos.append([codigo,quantidade,custo,preco])
    custos.append(custo)

maior_custo = max(custos)
n_posicao = custos.index(maior_custo)

if maior_custo == 0:
    print('nao tem compras')
else:
    print('Item mais caro')
    print('Codigo: {}'.format(produtos[n_posicao][0]))
    print('Quantidade: {:.0f}'.format(produtos[n_posicao][1]))
    print('Custo: {:.2f}'.format(produtos[n_posicao][2]))
