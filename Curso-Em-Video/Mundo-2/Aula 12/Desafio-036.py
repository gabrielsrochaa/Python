##Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
## O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
## Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado,

housevalue = int(input('\nDigite o valor da casa: \n R$'))
clientsalary = int(input('\nDigite o seu salário \n R$'))
yearspay = int(input('\nEm Quantos anos você pretende pagar a casa? \n'))
months = yearspay * 12
count1 = housevalue / months
percent1 = (clientsalary / 100) * 30

if count1 < percent1:
    print('\nParabéns, seu empréstimo foi aprovado! \nO valor da parcela é de R${:.2f} por mês pelo prazo de {} anos.'.format(count1, yearspay))
else:
    print('Infelizmente seu empréstimo não foi aprovado...')