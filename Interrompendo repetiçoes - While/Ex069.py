masc = muie = mais18 = 0
while True:
    print('-' * 30)
    print ('     CADASTRE UMA PESSOA     ')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('-'*30)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if sexo in 'Mm':
        masc = masc + 1
    if sexo in 'Ff' and idade < 20:
        muie = muie + 1
    if idade >= 18:
        mais18 = mais18 + 1
    if resp in 'Nn':
        break
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {masc} homens cadastrados')
print(f'E temos {muie} mulheres com menos de 20 anos')
