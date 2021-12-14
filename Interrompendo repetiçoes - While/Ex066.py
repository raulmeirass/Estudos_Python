c = soma = 0
while True:
    num = int(input('Digite um número: (999 pra parar) '))
    if num == 999:
        break
    soma = soma + num
    c = c + 1
print(f'A soma dos {c} valores foi {soma}!')
