times = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'Bragantino',
         'Fortaleza', 'Corinthians','Internacional', 'Fluminense',
         'Cuiabá', 'Ceará', 'Athletico-PR','América-MG',
         'Atlético-GO', 'São Paulo', 'Bahia', 'Santos',
         'Sport', 'Juventude', 'Grêmio', 'Chapecoense')
print('-=' * 20)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 20)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 20)
print(f'Os 4 ultimos são: {times[16:]}') #[-4:]
print('-=' * 20)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 20)
print(f'O chapecoense esta na {times.index("Chapecoense") + 1} posição')


