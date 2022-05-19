# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1=120
# import math

num = int(input('Digite um número para calcular seu fatorial: '))
# print(f'O fatorial de {numfactorial} é {math.factorial(numfactorial)}')
result = 0
c = num
f = 1
arr = []
while c > 0:
    result += num * c
    f *= c
    c -= 1
    arr.append(f'x {c}')
print(f'Calculando {num}! = {num} {prt} = {result}')
