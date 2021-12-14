nome = str(input('Qual é seu nome? '))
if nome == 'Raul':
    print ('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Luan' or nome == 'João' or  nome =='Arthur':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Maria Karla Luana Raissa': #in é igual o '='
    print ('Que belo nome feminino')
else:
    print('Seu nome é bem normal.')
print ('Tenha um bom dia, {}!'.format(nome))

