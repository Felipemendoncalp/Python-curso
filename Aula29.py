numero = input('Digite um numero  irei dobrar ele : ')
try:
    numero_string= float(numero)
    print('FLOAT', numero_string)
    print(f' O dobro de {numero} é {numero_string * 2}')
except :
    print('Isso não é um numero')