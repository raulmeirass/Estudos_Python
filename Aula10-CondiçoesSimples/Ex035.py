print ('-=' * 15)
print ('ANALISADOR DE TRIANGULOS')
print ('-=' * 15)
a = float (input('Primeiro segmento: '))
b = float (input('Segundo segmento: '))
c = float (input('Terceiro segmento: '))
if a < b + c and b < a + c and c < b + a:
    print('\033[34m Os segmentos acima PODEM FORMAR trinagulos!\033[m')
else:
    print ('\033[31m Os segmentos acima NÃO PODEM FORMAR triangulo!\033[m')
