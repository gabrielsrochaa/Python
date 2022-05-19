# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar advinhar até acertar,
# Mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep

count = 1
print('*'*100)
print('''Vou pensar em um número entre 0 e 10, você consegue advinhar qual é?! \n''')
numpc = randint(0, 10)
print('Estou pensando...\n')
sleep(2)
numuser = int(input('Pronto, tenta advinhar qual é o número: \n'))
if numuser == numpc:
    if count == 1:
        print(f'Parabéns, você acertou com {count} tentativa')
else:
    while numuser != numpc:
        numuser = int(input('Ops.. Você não acertou, tenta de novo: \n'))
        count += 1
if count > 1 :
    print(f'Parabéns, você acertou com {count} tentativas')
