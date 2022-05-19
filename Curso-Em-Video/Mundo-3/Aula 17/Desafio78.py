numbs = []
mai = 0
men = 0
for c in range(0,5):
    numbs.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = numbs[c]
    else:
        if numbs[c] > mai:
            mai = numbs[c]
        if numbs[c] < men:
            men = numbs[c]
print(f'\nVocê digitou os seguintes valores: {numbs}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(numbs):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor da lista foi {men} nas posições ', end='')
for i, v in enumerate(numbs):
    if v == men:
        print(f'{i}... ', end='')
print()