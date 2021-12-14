muie = 0
s = 0
maior = 0
for c in range (1, 5):
    print ('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    s = s + idade
    media = s / 4
    if sexo in 'Mm': #in é igual a =
        if idade > maior:
            maior = idade
            nomevelho = nome
    if sexo in 'Ff' and idade < 20:
            muie += 1
print('A média de idade do grupo é de {:.1f} anos.'.format(media))
print ('O homem mais velho tem {} anos e se chama {}'.format(maior, nomevelho))
print ('Ao todo são {} mulheres com menos de 20 anos'.format(muie))







