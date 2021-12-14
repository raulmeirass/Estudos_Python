nome = str (input('Nome do aluno:'))
n1 = float (input('Primeira nota do aluno{}:'.format (nome)))
n2 = float (input('Segunda nota do aluno{}:'.format (nome)))
m = (n1 + n2) / 2
print ('A média entre {} e {} é igual a {:.1f}.'.format (n1, n2, m))


