hora = input('Digite o hoarario em numeros inteiros ')
try:
    hora = int(hora)
    if hora >= 0 and hora  <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17 :
        print('Boa tarde')
    elif hora >= 18 and hora <=23 :
      print('Boa noite') 
except:
    print('Por favor, digite apenas um numero inteiro')
