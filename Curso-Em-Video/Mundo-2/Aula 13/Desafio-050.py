'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for impar, desconsidere-os'''
num1 = int(input('Digite um número: \n'))
num2 = int(input('Digite um número: \n'))
num3 = int(input('Digite um número: \n'))
num4 = int(input('Digite um número: \n'))
num5 = int(input('Digite um número: \n'))
num6 = int(input('Digite um número: \n'))

print('''\n Somando os números pares...''')
num_list = [num1, num2, num3, num4, num5, num6]
calc_list = 0

for c in range(len(num_list)):
    if num_list[c] % 2 == 0:
        calc_list += num_list[c]
print('\n A soma de todos os VALORES PARES digitados é {}'.format(calc_list))
