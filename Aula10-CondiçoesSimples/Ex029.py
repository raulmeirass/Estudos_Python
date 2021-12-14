vel = float(input('Qual é a velocidade atual do carro (km/h)?'))
if vel > 80:
    multa = (vel - 80) * 7
    print ('\033[33;40mMULTADO! Voce excedeu o limite permitido que é de 80km/h!\033[m')
    print ('O valor da multa é de R${:.2f}!'.format(multa))
print('Tenha um bom dia, dirija com segurança!')
