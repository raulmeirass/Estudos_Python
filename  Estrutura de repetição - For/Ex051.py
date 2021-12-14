print('=' * 40)
print('10 TERMOS DE UMA PA')
print('=' * 40)
prim = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = prim + (10 - 1) * razao
for c in range (prim, decimo + razao,razao):
    print (c, end=' -> ')
print(' ACABOU ')



