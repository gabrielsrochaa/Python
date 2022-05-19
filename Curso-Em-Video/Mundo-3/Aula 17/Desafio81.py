numbsList = []
choice = 0
while True:
    num = int(input('Digite um valor: '))
    choice = str(input('Quer continuar? [S/N] ')).upper()
    numbsList.append(num)
    if choice in 'Nn':
        break
print('#'*100)
print(f'Você digitou {len(numbsList)} elementos.')
numbsList.sort(reverse=True)
print(f'Os valores em ordem descrescente são {numbsList}')
if 5 in numbsList:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')