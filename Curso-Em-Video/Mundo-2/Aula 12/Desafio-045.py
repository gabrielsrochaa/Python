"""Crie um programa que faça o computador jogar jokenpô com você"""

import random

print('''     
                                --------- 
                                |Jokenpô|
                                ---------          
\nVamos lá, você tem 3 opções abaixo, escolha uma delas e tente derrotar o computador:\n
                      1 - Pedra
                      2 - Papel
                      3 - Tesoura                  ''')

options = ['Pedra', 'Papel', 'Tesoura']
user_choice = int(input('\nEscolha uma das opções acima: \n'))

pc_choice = random.choices(options)

if user_choice == 1 and pc_choice[0] == 'Tesoura':
    user_choice = 'Pedra'
    print('\nVitória!\n Você venceu, você escolheu {} e o computador escolheu {}'.format(user_choice, pc_choice[0]))
elif user_choice == 1 and pc_choice[0] == 'Papel':
    user_choice = 'Pedra'
    print('\nDerrota!\n Você escolheu {} e o computador escolheu {}'.format(user_choice, pc_choice[0]))
elif user_choice == 1 and pc_choice[0] == 'Pedra':
    user_choice = 'Pedra'
    print('\nEmpate!\n Você escolheu {} e o computador escolheu {}'.format(user_choice, pc_choice[0]))
elif user_choice == 2 and pc_choice[0] == 'Pedra':
    user_choice = 'Papel'
    print('\nVitória!\n Você venceu, você escolheu {} e o computador escolheu {}'.format(user_choice, pc_choice[0]))
elif user_choice == 2 and pc_choice[0] == 'Papel':
    user_choice = 'Papel'
    print('\nEmpate!\n Você escolheu {} e o computador escolheu {}'.format(user_choice, pc_choice[0]))
elif user_choice == 2 and pc_choice[0] == 'Tesoura':
    user_choice = 'Papel'
    print('\nDerrota!\n Você escolheu {} e o computador escolheu {}'.format(user_choice, pc_choice[0]))
elif user_choice == 3 and pc_choice[0] == 'Pedra':
    user_choice = 'Tesoura'
    print('\nDerrota!\n Você escolheu {} e o computador escolheu {}'.format(user_choice, pc_choice[0]))
elif user_choice == 3 and pc_choice[0] == 'Papel':
    user_choice = 'Tesoura'
    print('\nVitória!\n Você venceu, você escolheu {} e o computador escolheu {}'.format(user_choice, pc_choice[0]))
elif user_choice == 3 and pc_choice[0] == 'Tesoura':
    user_choice = 'Tesoura'
    print('\nEmpate!\n Você escolheu {} e o computador escolheu {}'.format(user_choice, pc_choice[0]))
elif user_choice != 1 or user_choice != 2 or user_choice != 3:
    print('\nVocê não escolheu uma opção válida! \n Por favor tente novamente...')
