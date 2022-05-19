numbsList = []
pairNumbs = []
noPairNumbs = []
choice = 0

while True:
    num = int(input('Digite um valor: '))
    numbsList.append(num)
    choice = str(input('Quer continuar? [S/N] ')).upper()
    if choice in 'Nn':
        break
for c in numbsList:
    if c % 2 == 0:
        pairNumbs.append(c)
    else:
        noPairNumbs.append(c)
numbsList.sort()
pairNumbs.sort()
noPairNumbs.sort()
print('#'*100)
print(f'A lista completa é {numbsList}')
print(f'A lista de pares é {pairNumbs}')
print(f'A lista de ímpares é {noPairNumbs}')