#!/usr/bin/python3
#try:
with open('teste.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()

with open('teste.txt', 'w') as arquivo:
    cont = 1
    for x in conteudo:
        arquivo.write("{}- {}".format(cont,x))
        cont += 1 
