#nome = 'Otávio'
#print(nome[2])
# print(nome[-4])

# print('á' in nome)
# print('zero' in nome)
# print(10* '-')
# print('f' not in nome)

nome= input('Digite o que deseja encontrar: ')
encontrar = input('Digite o que deseja encontar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

