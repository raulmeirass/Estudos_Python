lista = ('doce', 5.00,
         'bala',  2.00,
         'chocolate', 3.00,
         'pirulito', 1.50,
         'fini', 4)
print('-'*40)
print(f'{"LISTAGEM DE PRODUTOS":^40}') #centraliza em 40 espaços
print('-'*40)
for item in range (0, len(lista)): #for consege "separar as tuplas"
    if item % 2 == 0: #os num pares são as posiçoes dos produtos (0, 2, 4, 6)
        print(f'{lista[item]:.<30}', end='') #colocar os itens e depois coloca 30 pontos (.) pra direita
    else: #os num impares são as posiçoes dos preços (1, 3, 5)
        print(f'R${lista[item]:>7.2f}') #7espaços pra esquerda e depois colocar o preço
print('-'*40)

