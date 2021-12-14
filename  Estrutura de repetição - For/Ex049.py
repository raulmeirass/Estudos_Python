num = int(input('Digite um número para ver a sua tabuada: '))
s = 0
for c in range (1, 11):
    s = s + 1
    tab = s * num
    print('{} x {} = {}'.format(s, num, tab))
 #-> OU
#num = int(input('Digite um número para ver a sua tabuada: '))
#for c in range (1, 11):
#print('{} x {} = {}'.format(num, c, num*c))

 