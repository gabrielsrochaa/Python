numbsList = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > numbsList[-1]:
        numbsList.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numbsList):
            if num <= numbsList[pos]:
                numbsList.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('#'*100)
print(f'Os valores digitados em ordem foram {numbsList}')