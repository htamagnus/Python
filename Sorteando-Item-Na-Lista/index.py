#DESAFIO 19: SORTEANDO UM ITEM NA LISTA
"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido."""
import random
n1 = str(input('Primeira opção: '))
n2 = str(input('Segunda opção: '))
n3 = str(input('Terceira opção: '))
n4 = str(input('Quarto opção: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('A opção escolhida foi {}'.format(escolhido))