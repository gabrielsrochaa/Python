numbsList = []
choice = 0
while choice != 'N':
    numbs = int(input('Digite um valor: '))
    if numbs not in numbsList:
        numbsList.append(numbs)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não será adicionado...')
    choice = str(input('Quer continuar? [S/N] ')).upper()
numbsList.sort()
print('#'*100)
print(f'Você digitou os valores {numbsList}')
