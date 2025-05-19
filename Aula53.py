lista = ['Maria', 'Helena', 'Felipe']
lista.append('Luiz')
lista_enumerada = enumerate(lista, start=10)
print(next(lista_enumerada))
for indice , nome in enumerate(lista) :
    #indice , nome = item
    #print(item)
    print(indice, nome)
    
# for item in enumerate(lista):
#     for valor in item : 
#         print(valor)