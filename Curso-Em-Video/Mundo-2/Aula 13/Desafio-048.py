# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três...
#  E que se encontram no intervalo de 1 até 500

print('Somando todos os números ímpares que são múltiplos de 3\n')
imp_sum = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        imp_sum += c
print(f'A soma de todos os {cont} valores solicitados é {imp_sum}')
