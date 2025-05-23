salas = [
    ['Felipe' , 'luiz'],

    ['Cleiton', 'Jackson'],
    #['Cleiton', 'Jackson',(10,20,30,40)],
]
#print(salas[1][2][3])
for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)