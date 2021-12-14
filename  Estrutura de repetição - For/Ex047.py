s = 0
for c in range (1, 51):

    if c % 2 == 0:
        s = s + 1
        print(c, end=' ') #end=' ' pra ficar na mesma linha
print('\n Existem {} números pares entre 1 e 50.'.format(s)) #\n pra quebrar a linha

