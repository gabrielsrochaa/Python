# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa mostre:
# - A média de idade do grupo
# - Qual é o homem mais velho
# - Quantas mulheres tem menos de 20 anos.

agesum = 0
oldestManAge = 0
oldestManName = ''
totalWoman20 = 0
for p in range(1, 5):
    print(f'----- {p}ª Pessoa -----')
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    gen = str(input('Sexo [M/F]: ')).strip()
    agesum += age
    if p == 1 and gen in 'Mm':
        oldestManAge = age
        oldestManName = name
    if gen in 'Mm' and age > oldestManAge:
        oldestManAge = age
        oldestManName = name
    if gen in 'Ff' and age < 20:
        totalWoman20 += 1

agemedia = agesum / 4
print(f'A média de idade do grupo é de {agemedia} anos')
print(f'O homem mais velho tem {oldestManAge} anos e se chama {oldestManName}')
print(f'Ao todo são {totalWoman20} mulheres com menos de 20 anos')