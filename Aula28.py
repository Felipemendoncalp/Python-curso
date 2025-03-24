nome = input('Digite seu nome : ')
idade = input('Digite sua idade : ')

if nome and idade  :
    print(f'Seu nome é {nome}')
    print(f'Sua idade é de {idade} anos')
    print(f'Seu nome ivertido é {nome[::-1]}')
    if ' ' in nome :
        print(f'Seu nome contem espaços')
    else :
        print(f'Seu nome não contem espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome {nome [0]}')
    print(f'A ultima letra do nome é {nome[-1]}')
else :
    print('Desculpe, você deixou campos vazios')