numero =input('Digite um numero inteiro : ')

if numero.isdigit() :
    numero = int(numero)
    par_impar = numero % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto ='par'
    print(f'O numero {numero} é {par_impar_texto}')
else:
    print('Você não digitou um numero inteiro:')