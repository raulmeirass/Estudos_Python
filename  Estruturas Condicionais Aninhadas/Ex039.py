from datetime import date
atual = date.today().year #para saber o ano atual
nasc = int(input('Ano de nascimento: '))
sexo = int(input('Digite [ 1 ] se voce for homem e [ 2 ] se for mulher: '))
idade = atual - nasc
print ('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if sexo == 2:
    print ('Voce não precisa se alistar!')
if idade == 18 and sexo == 1:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18 and sexo == 1:
    falta = 18 - idade
    print ('Ainda faltam {} anos para o seu alistamento'.format(falta))
    ano = atual + falta
    print ('Seu alistamento será em {}'.format(ano))
elif idade > 18 and sexo == 1:
    passou = idade - 18
    print('Voce ja deveria ter se alistado há {} anos.'.format(passou))
    ano = atual - passou
    print ('Seu alistamento foi em {}'.format(ano))
print ('  ')
print('OBRIGADO! Tenha um ótimo dia.')



