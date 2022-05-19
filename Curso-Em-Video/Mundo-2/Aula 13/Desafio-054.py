'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
totalMinors = 0
totalMajors = 0
actualyear = date.today().year
for c in range(1, 8):
    person = int(input(f'Em que ano a {c}ª pessoa nasceu?\n'))
    age = actualyear - person
    if age >= 21:
        totalMajors += 1
    else:
        totalMinors += 1
print(f'\n A quantidade de pessoas que não atingiram a maioridade é {totalMinors}')
print(f'\n A quantidade de pessoas que já são maiores é {totalMajors}')



