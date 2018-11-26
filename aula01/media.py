#!/usr/bin/python3
nota1 = int(input('entre com a nota 1: '))
nota2 = int(input('entre com a nota 2: '))
media = (nota1+nota2)/2
if media >= 7:
    print('Aprovado')
elif media < 7 and media > 3:
    print('Recuperaçao')
else:
    print('Reprovado')


