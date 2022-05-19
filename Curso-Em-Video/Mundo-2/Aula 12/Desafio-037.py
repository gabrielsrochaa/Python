##Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
## - 1 para binário
## - 2 para octal
## - 3 para hexadecimal

num1 = int(input('Digite um número inteiro: \n'))
select = int(input('''\nSelecione a base de conversão: 
\n1 para converter o número para binário \n2 para converter o número para octal \n3 para converter o número para hexadecimal \n'''))

if select == 1:
    print('O número {} convertido para binário é {}'.format(num1, bin(num1)[2:]))
elif select == 2:
    print('O número {} convertido para octal é {}'.format(num1, oct(num1)[2:]))
elif select == 3:
    print('O número {} convertido para hexadecimal é {}'.format(num1, hex(num1)[2:]))
else:
    print('Você não selecionou uma base de conversão válida, por favor tente novamente...')