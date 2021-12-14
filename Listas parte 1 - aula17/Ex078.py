num = list() #ou []
maior = 0
menor = 0
for cont in range (0,5):
    num.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = num[cont]
    else:
        if num[cont] > maior:
            maior = num[cont]
        if num[cont] < menor:
            menor = num[cont]
print('-=' * 30)

print(f'Voce digitou os valores {num}')
print(f'O maior valor digitado foi o {maior} nas posições ', end='')
for c, v in enumerate(num):
    if num[c] == maior: #numero na posição c (0,1, 2, 3, 4)
        print(f'{c}...', end='')
print()
print(f'O menor valor digitado foi o {menor} nas posiçoes ', end='')
for c, v in enumerate (num):
    if num[c] == menor:
        print(f'{c}...', end='')




