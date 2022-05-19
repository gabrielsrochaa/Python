##A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
## - Até 9 anos: MIRIM
## - Até 14 anos: INFANTIL
## - Até 19 anos: JUNIOR
## - Até 20 anos: SENIOR
## - Acima: MASTER

from datetime import datetime


yearborn = int(input('Digite seu ano de nascimento: \n'))
actualyear = datetime.today()

age = actualyear.year - yearborn

if age <= 9:
    print('MIRIM')
elif age > 9 and age <= 14:
    print('INFANTIL')
elif age > 14 and age < 19:
    print('JUNIOR')
elif age == 20:
    print('SENIOR')
elif age > 20:
    print('MASTER')