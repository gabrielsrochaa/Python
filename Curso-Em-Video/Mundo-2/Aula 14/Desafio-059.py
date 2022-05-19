# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
option = 0

while option != 5:
    option = int(input('''    
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

>>>>> Qual é a sua opção? '''))
    if option == 1:
        result = num1 + num2
        print(f'A soma entre {num1} e {num2} é igual a {result}')
    elif option == 2:
        result = num1 * num2
        print(f'A multiplicação entre {num1} e {num2} é igual a {result}')
    elif option == 3:
        result = [num1, num2]
        print('*'*100)
        print(f'\nO maior número digitado é {max(result)}')
    elif option == 4:
        num1 = int(input('Digite o novo primeiro número: '))
        num2 = int(input('Digite o segundo novo número: '))
    elif option == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
#     option = int(input('''Qual operação você deseja realizar com os número digitados?
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# '''))