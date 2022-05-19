##Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
## - Se ele ainda vai se alistar ao serviço militar.
## - Se é a hora de se alistar.
## - Se já passou do tempo do alistamento.
## Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date, datetime

bornyear = int(input('Digite o seu ano de nascimento: \n'))
count1 = date.today().year
age = count1 - bornyear

if age < 18:
    print('\nQuem nasceu em {} tem {} anos em {} \n Você ainda não se alistou!'.format(bornyear, age, count1))
elif age == 18:
    print('\nQuem nasceu em {} tem {} anos em {} \n Você precisa se alistar IMEDIATAMENTE!\n'.format(bornyear, age, count1))
elif age > 18:
    print('\nQuem nasceu em {} tem {} anos em {} \nA hora de se alista já passou!\n'.format(bornyear, age, count1))