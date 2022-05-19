# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteha errado, peça a digitação novamente até ter um valor correto.
gen = str(input('Informe o seu sexo: [M/F] \n')).strip()
if gen.upper() == 'M' or gen.upper() == 'F':
    print('FIM')
else:
    while gen != 'M' or gen != 'F':
        print('Opção inválida! \n Por favor, digite novamente uma das opções [M/F]...')
        gen = str(input('Qual é o seu sexo [M/F]? \n'))