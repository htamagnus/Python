#Programa que lê as quatro opções e mostre a ordem sorteada.
n1 = str(input('Primeira opção: '))
n2 = str(input('Segunda opção: '))
n3 = str(input('Terceira opção: '))
n4 = str(input('Quarto opção: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será')
print(lista)