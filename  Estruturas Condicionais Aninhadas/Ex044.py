print('{:=^40}'.format(' LOJAS RAUL ')) #{:^40} para centralizar o nome da loja no meio e o = para colocar dos lados
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opc = int(input('Qual foi a opção? '))
if opc == 1:
    valor = preço - (preço/100 * 10)
elif opc == 2:
    valor = preço - (preço/100 * 5)
elif opc == 3:
    valor = preço
    parc = valor/2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parc))
elif opc == 4:
    parc = int(input('Quantas parcelas? '))
    valor = preço + (preço * 20 / 100)
    juros = valor / parc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parc, juros))
else:
    valor = preço
    print('OPÇÃO INVALIDA de pagamento, tente novamente!')
print ('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, valor))

