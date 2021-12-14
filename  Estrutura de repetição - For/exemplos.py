#inicio = int(input('Inicio: '))
#fim = int(input('Fim: '))
#passo = int(input('Passo: '))
#for c in range (inicio, fim+1, passo):
#    print(c)
#print ('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s = s + n #ou s+=n
print('O somatório de todos os valores foi {}'.format(s))

