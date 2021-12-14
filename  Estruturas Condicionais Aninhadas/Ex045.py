import random
from time import sleep
print('-=' * 11)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jog = int(input('Qual a sua jogada? '))
print ('JO')
sleep (0.4)
print ('KEN')
sleep (0.4)
print ('PO!!!')
print('-=' * 13)
num = random.randint(0, 2) #faz o computador ""pensar""
if num == 0:
    print('Computador jogou PEDRA')
elif num == 1:
    print('Computador jogou PAPEL')
elif num == 2:
    print ('Computador jogou TESOURA')

if jog == 0:
    print('Jogador jogou PEDRA')
elif jog == 1:
    print('Jogador jogou PAPEL')
elif jog == 2:
    print('Jogador jogou TESOURA')
print('-=' * 13)
if num == 0 and jog == 2 or num == 1 and jog == 0 or num == 2 and jog == 1:
    print('COMPUTADOR VENCE!')
elif jog == 0 and num == 2 or jog == 1 and num == 0 or jog == 2 and num == 1:
    print('JOGADOR VENCE!')
elif jog == num:
    print ('EMPATE!')




