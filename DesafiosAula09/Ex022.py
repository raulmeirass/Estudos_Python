nome = str (input('Digite seu nome completo:')).strip()
print ('Analisando seu nome...')
print ('Seu nome em maiusculas é', nome.upper())
print ('Seu nome em minusculas é', nome.lower())
print ('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
divisao = nome.split()
print ('Seu primeiro nome é {} e ele tem {} letras'.format(divisao [0],len(divisao [0])))




