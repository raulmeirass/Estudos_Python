s = 0
valor = 0
for c in range (1, 501, 2): #o 2 é pra pular de impar pra impar a partir do 1
    if c % 3 == 0:
        s = s + c # ou s =+ c
        valor = valor + 1 # ou valor += 1
print ('A soma de todos os {} valores solicitados foi {}'.format(valor, s))
