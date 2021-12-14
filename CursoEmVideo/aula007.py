n2 = int (input ('Digite um número: '))
n1 = int (input ('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
div = n1 // n2
pot = n1 ** n2
print ('Soma é {}, \n produto é {}, \n e divisão é {:3}' .format (s, m, d), end= " >>> ")
print ('Divisão inteira {}, \n e potencia {}' .format (div, pot))
