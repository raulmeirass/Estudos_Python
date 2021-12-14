n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2) / 2
print ('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media >= 7.0:
    print('aluno APROVADO!')
elif 5.0 <= media < 7.0:
    print ('Aluno de RECUPERAÇÃO!')
elif media < 5.0:
    print ('Aluno REPROVADO!')
    