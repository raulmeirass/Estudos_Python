import random
print('''Olá, sou seu computador... Acabei de pensar em um número entre 0 a 10.
Será que voce consegue adivinhar qual foi?''')
comput = random.randint(0,10)
soma = 0
palp = 11
while palp != comput:
    palp = int(input('Qual é o seu palpite? '))
    soma = soma + 1
    if palp > comput:
        print('Menos... Tente mais uma vez')
    elif palp < comput:
        print('Mais... Tente mais uma vez')
print ('Voce acertou em {} tentativas. Parabens!'.format(soma))






