import random
from time import sleep

num = random.randint(0, 5) #faz o computador ""pensar""
print ('-' * 52)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar')
print ('-' * 52)
numero = int (input('Em que número pensei?'))
print ('PROCESSANDO...')
sleep (1.5)
if numero == num:
    print('\033[36;47mPARABENS! Voce conseguiu me vencer!\033[m')
else:
    print('\033[31;47m GANHEI! Eu pensei no número {} e não no {}!\033[m'.format(num, numero))



