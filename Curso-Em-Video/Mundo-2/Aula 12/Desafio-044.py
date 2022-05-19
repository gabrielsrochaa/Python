## Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
## - à vista dinheiro/cheque: 10% de desconto
## - à vista no cartão: 5% de desconto
## - em até 2x no cartão: preço normal
## - 3x ou mais no cartão: 20% de juros

productvalue = float(input('Qual é o valor do produto? \nR$'))

payment_method = int(input('''
                           ****Selecione o método de pagamento****
                          | 1 - À vista dinheiro/cheque |
                          | 2 - À vista no cartão       |
                          | 3 - Em até 2x no cartão     |
                          | 4 - 3x ou mais no cartão    |
                           '''))

if payment_method == 1:
    discount_value = (productvalue / 100) * 10
    final_value = productvalue - discount_value
    print('Você recebeu um desconto de 10%, com isso o valor final do produto é R${}'.format(final_value))
elif payment_method == 2:
    discount_value = (productvalue / 100) * 5
    final_value = productvalue - discount_value
    print('Você recebeu um desconto de 5%, com isso o valor final do produto é R${}'.format(final_value))
elif payment_method == 3:
    final_value = productvalue
    print('O valor final do produto é R${}'.format(final_value))
elif payment_method == 4:
    discount_value = (productvalue / 100) * 20
    final_value = productvalue + discount_value
    print('o valor final do produto é R${}'.format(final_value))