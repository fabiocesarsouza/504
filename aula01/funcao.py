#!/usr/bin/python3
def ler_arquivo(arquivo):
    with open(arquivo, 'r') as arq:
        return arq.readlines()

def escrever_arquivo(texto, arquivo='novo.txt'):
    with open(arquivo, 'a') as arq:
        arq.write(texto)

def contar_linhas(arquivo):
    return ler_arquivo(arquivo).__len__()





escrever_arquivo('ola isso é um teste\n')
escrever_arquivo('ola isso é outro teste\n')
print(ler_arquivo('novo.txt'))
print(contar_linhas('novo.txt'))

