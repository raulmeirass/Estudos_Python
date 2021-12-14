nome = 'raul'
cores = {'limpar': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'preto': '\033[7;30m'}
print ('Olá {}{}{}'.format(cores['preto'], nome, cores['limpar']))
