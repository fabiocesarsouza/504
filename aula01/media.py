#!/usr/bin/python3

qtdenotas = int(input('Qual a quantidade de notas? '))
soma = 0
for x in range(qtdenotas):    
    try:
        notas = int(input('entre com a nota {}: '.format(x+1)))
    except ValueError:
        print('Nota invalida')  
        exit()

for nota in range(qtdenotas): 
    soma += notas
media = soma/x
if media >= 7:
    print('Aprovad, media {}'.format(media))
elif media < 7 and media > 3:
    print('Recuperaçao, media {}'.format(media))
else:
    print('Reprovado, media {}'.format(media))


