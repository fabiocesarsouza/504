#!/usr/bin/python3
nome = ''
lista = []
while True:
    nome = input('Entre com um nome: ')
    if nome == 'sair':
        break
    else:
        lista.append(nome)

print(lista)