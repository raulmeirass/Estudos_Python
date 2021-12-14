a = float (input('Primeiro segmento: '))
b = float (input('Segundo segmento: '))
c = float (input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triangulo', end=' ')
    if a == b == c:
        print('EQUILATERO!')
    elif a != b != c != a:
        print ('ESCALENO!')
    if a == b and a != c or b == c and b != a or a == c and c != b: #poderia colocar só o "else"
        print('ISOSCELES!')
else:
    print('\033[31m Os segmentos acima NÃO PODEM FORMAR triangulo!\033[m')
