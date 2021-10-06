#DESAFIO 10: CONVERSOR DE MOEDAS
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.26
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))