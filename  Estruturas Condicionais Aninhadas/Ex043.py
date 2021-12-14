peso = float(input('Qual o seu peso? (Kg) '))
alt = float (input('Qual a sua altura? (m) '))
imc = peso / (alt * alt) #alt ** 2
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta ABAIXO do PESO normal!')
elif 18.5 <= imc < 25:
    print('PARABENS, voce esta na faixa de PESO NORMAL!')
elif 25 <= imc < 30:
    print('Voce esta em SOBREPESO')
elif 30 <= imc < 40:
    print('Voce esta em OBESIDADE!')
elif imc >= 40:
    print('Voce esta em OBESIDADE MÓRBIDA, cuidado!')


