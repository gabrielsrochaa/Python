nome = str(input("Qual é o seu nome? \nR: "))

if nome == "Gabriel":
    print("\nQue nome lindo!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("\nSeu nome é bem comum no Brasil.")
elif nome in 'Ana Cláudia Jéssica Juliana':
    print("Belo nome feminino")
else:
    print('Seu nome é bem normal!')

print("\nTenha um bom dia, {}!\n ".format(nome))