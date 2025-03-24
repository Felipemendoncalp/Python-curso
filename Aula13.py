nome = 'Felipe Lopes'
altura= 1.73
peso = 58
imc = peso / (altura ** 2)
#f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é {imc}'
print(linha_1)
print(linha_2)
print(nome, 'tem', altura ,'De altura, pesa' , peso, ' quilos e seu IMC é', imc)
print(f'{nome} tem {altura} de altura pesa {peso} e seu IMC é {imc}')
