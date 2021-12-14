import math
angulo = float(input('Digite o valor do angulo:'))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tang))