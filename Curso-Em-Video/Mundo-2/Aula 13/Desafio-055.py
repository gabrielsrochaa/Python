'''Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior peso lidos.'''

peso1 = 0
list1 = []

for c in range(0, 5):
    peso1 = float(input(f'Peso da {c+1}ª pessoa? \n'))
    list1.append(peso1)

print(f'\nO maior peso lido foi {max(list1)}Kg')
print(f'\n0 meno peso lido foi {min(list1)}kg')