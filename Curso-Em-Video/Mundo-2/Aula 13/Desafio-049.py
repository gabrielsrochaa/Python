num1 = int(input('Digite um número para saber a tabuada dele: \n'))
print('TABUADA do número {}'.format(num1))
tab = 0
for c in range(0, 10):
    tab += 1
    print('{} x {} = {}'.format(num1, tab, num1 * tab))
