express = str(input('Digite a expressão: '))
# lista = ' '.join(express).split()
# count_parenthesis = 0
# for parenthesis in lista:
#     if '(' in parenthesis:
#         count_parenthesis += 1
#     if ')' in parenthesis:
#         count_parenthesis += 1
# if count_parenthesis % 2 == 0:
#     print('Sua expressão é válida!')
# else:
#     print('Sua expressão está errada!')
pilha = []
for simb in express:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
