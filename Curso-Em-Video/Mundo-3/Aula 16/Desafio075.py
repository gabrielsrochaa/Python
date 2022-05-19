num = int(input(f'Digite o primeiro valor: ')), int(input(f'Digite o segundo valor: ')), \
      int(input(f'Digite o terceiro valor: ')), int(input(f'Digite o quarto valor: '))

print(f'\nO valor 9 apareceu {num.count(9)} vezes. \n')

if num.count(3) > 1:
    print(f'O valor 3 foi digitado na posição {num.index(3)+1}.\n')
else:
    print(f'O valor 3 não foi digitado.\n')

print(f'Os número pares são: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end='')
