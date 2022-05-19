'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
cousin_number = int(input('Digite um número para saber se ele é um número primo: \n'))
list_primos = 0
for c in range(0, 1):
    if cousin_number % 1 == 0 and cousin_number % cousin_number == 0:
        if cousin_number % 2 != 0 and cousin_number % 3 != 0 and cousin_number % 5 != 0 and cousin_number % 7 != 0:
            list_primos += cousin_number
            print('O número {} é PRIMO'.format(list_primos))
        else:
            print('O número {} não é PRIMO'.format(cousin_number))

#for c in range(0, cousin_number):
#    if cousin_number % 2 == 0
#        print('O número {} não é PRIMO!'.format(cousin_number))
#    elif cousin_number % 1 == 0 and cousin_number % cousin_number == 0:
#        print('O número {} é um PRIMO!')
