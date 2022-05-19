## Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
## de acordo com a média atingida:
## - Média abaixo de 5.0: REPROVADO
## - Média entre 5.0 e 6.9: Recuperação
## - Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota do(a) aluno(a): \n'))
nota2 = float(input('Digite a segunda nota do(a) aluno(a): \n'))

media = (nota1 + nota2) / 2
print(media)

if media <= 4.9:
    print('Tirando {} e {}, a média do aluno é {} \n O aluno está REPROVADO'.format(nota1, nota2, media))
elif media >= 5.0 and media <= 6.9:
    print('Tirando {} e {}, a média do aluno é {} \n O aluno está em RECUPERAÇÃO'.format(nota1, nota2, media))
elif media >= 7.0:
    print('Tirando {} e {}, a média do aluno é {} \n O aluno está APROVADO'.format(nota1, nota2,media))