'''Crie um programa que leia uma frase qyalquer e diga se ela é um palíndromo, desconsiderando os espaços.
Ex:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA'''

phrase = str(input('Digite uma frase ou uma palavra e descubra se ela é um palíndromo: \n'))
phrasen = phrase.split()
collect_letters_list = ''.join(phrasen)
collect_letters = []
for c in reversed(range(len(collect_letters_list))):
    collect_letters += collect_letters_list[c]
conv_list = ''.join(map(str, collect_letters))
if conv_list[0:len(conv_list)] == ''.join(phrasen):
    print('{} é um palíndromo, pois pode ser lido de trás para frente e continua exatamente igual!'.format(phrase))
else:
    print('{} não é um palíndromo, pois não pode ser lido de trás para frente'.format(phrase))
print(conv_list[0:len(conv_list)])
