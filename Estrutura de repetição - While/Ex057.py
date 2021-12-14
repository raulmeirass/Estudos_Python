'''sexo = 'n'
while sexo not in 'FM': #not in -> É não é igual
    sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0] #[0] só pega a primeira letra
    if sexo == 'F' or sexo == 'M':
        print('Sexo {} registrado com sucesso!'.format(sexo))
    else:
        print('Dados invalidos. Por favor,',end=' ')'''

sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'FM':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: [M/F] ')).upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
