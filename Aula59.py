string = 'ABCD'
lista = ['Maria', 'Helena', 1,2,3, 'Eduarda' ]
#p,b,*_,ap,u = lista
#print(p,u,ap)
for nome in lista:
    print(nome,end=' ')
print(*lista)
print(*string)
