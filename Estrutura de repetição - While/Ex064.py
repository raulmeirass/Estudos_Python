cont = soma = 0
num = int(input('Digite um número [999 pra parar]: '))
while num != 999:
    soma = soma + num
    cont = cont + 1
    num = int(input('Digite um número [999 pra parar]: '))
print('Voce digitou {} números e a soma entre eles foi {}'.format(cont, soma))

