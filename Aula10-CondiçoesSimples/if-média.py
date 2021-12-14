n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print ('A sua média foi: {:.1f}'.format(m))
if m >= 6.0:
    print ('\033[34;40mSua média foi BOA, PARABENS!\033[m')
else:
    print ('\033[31;40mSua média foi RUIM, ESTUDE MAIS!\033[m')

#print('PARABENS!' if m>=6.0 else 'ESTUDE MAIS!')

