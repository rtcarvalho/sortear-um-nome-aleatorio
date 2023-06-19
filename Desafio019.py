print('Um professor quer sortear um dos seus quatro aluno apara apagar o quadro.'
      'Faça um programa que ajude ele lendo o nome dele e escrevendo o nome do escolhido.')

import random
alunos = ['Raphael', 'Luiz','Bill','Andre']
professor = input('Digite o nome do professor: ')

print('Olá professor {}!'.format(professor))
sorteado = random.choice(alunos)
print('O aluno sorteado foi {}'.format(sorteado))

#segunda forma

from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]
escolha = choice(lista)
print("O aluno escolhido foi {}".format(escolha))


