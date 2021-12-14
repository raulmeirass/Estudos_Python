'''opos = float (input('Comprimento do cateto oposto:'))
adj = float (input('Comprimento do cateto adjacente:'))
hipo = (opos**2 + adj**2) ** (1/2)
print ('A hipotenusa vai medir {:.2f}'.format(hipo))'''

import math
opos = float (input('Comprimento do cateto oposto:'))
adj = float (input('Comprimento do cateto adjacente:'))
hipo = math.hypot(opos, adj)
print ('A hipotenusa vai medir {:.2f}'.format(hipo))
