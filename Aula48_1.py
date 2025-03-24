# lista = [10,20,30,40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
# lista.append(50)
# lista.pop()
# lista.append(60)
# lista.insert(0,5)
# print(lista)

lista_a = [1,2,3]
lista_b = lista_a.copy()
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_b)