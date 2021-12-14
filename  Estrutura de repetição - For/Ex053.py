frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #split para dividir a frase e colocar cada palavra em uma lista
junto = ''.join(palavras) #join p unir de novo mas sem espaços, em só uma string
inverso = '' #variavel
for letra in range (len(junto) - 1, -1, -1): #ultima letra, primeira letra, vai pra tras pulando 1 letra
    inverso = inverso + junto[letra] #tras p frente -> inverso; [] pq tinha virado lista
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase dgitada não é um palindromo')
 #OU no lugar de inverso = '' até o for e o inverso = inverso + junto...
 #poderia usar:
 #inverso = junto[::-1]