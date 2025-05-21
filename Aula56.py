frase = 'Olha so que , coisa interessante'
lista_palavras_cruas = frase.split(',')
lista_palavras = []
for i,frase in enumerate(lista_palavras_cruas):
    lista_palavras.append(lista_palavras_cruas[i].rstrip())
    print(lista_palavras_cruas[i])
frases_unidas = '-'.join(lista_palavras)
print(frases_unidas)