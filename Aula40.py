while True:
    numero_1 = input('Digite um numero ')
    numero_2 = input('Digite outro numero ')
    operador = input('Digite o operador (+-/*): ')
    numeros_validos = None
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
# valida se os numeros não do tipo float
    if numeros_validos is None:
        print('Um ou ambos números digitados são invalidos. ')
        continue
    operadores_permitidos = "+-/*"
#validas os operados 
    if operador not in operadores_permitidos :
        print('Operador invalido')
        continue
#valida se o usuario digitou apenas um operador
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
#Realização  das contas
    print('Realizando sua conta confira a abaixo')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float}  = ', num_1_float + num_2_float )
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = ', num_1_float - num_2_float )
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = ', num_1_float * num_2_float )
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = ', num_1_float / num_2_float )
    
    sair = input('Quer sair? [s]sim :').lower().startswith('s')
    
    if sair is True:
        break