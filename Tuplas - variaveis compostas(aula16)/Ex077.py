nomes = ('pyhton', 'raul', 'livro', 'karla', 'curso',
         'book', 'lituania')

for n in nomes:
    print(f'\nNa palavra {n.upper()} temos ', end='')
    for vog in n:
        if vog.lower() in 'aeiou':
            print(vog, end=' ')




