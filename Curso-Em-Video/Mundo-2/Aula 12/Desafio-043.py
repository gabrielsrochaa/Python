##Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
## - Abaixo de 18.5: Abaixo do peso
## - Entre 18.5 e 25: Peso ideal
## - 25 até 30: Sobrepeso
## - 30 até 40: Obesidade
## - Acima de 40: Obesidade Mórbida

altura = float(input('Informe a sua altura: \n'))
peso = float(input('Informe o seu peso: \n'))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Seu IMC é {:.1f}, você está abaixo do peso'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é {:.1f}, você está com o peso ideal'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é {:.1f}, você está com sobrepeso'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC é {:.1f}, você está com obesidade'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.1f}, você está com obesidade mórbida'.format(imc))