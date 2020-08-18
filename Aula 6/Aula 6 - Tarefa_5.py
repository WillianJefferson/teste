nome = input('Digite um nome: ')
nome = nome.upper()
n = nome
for i in range(len(nome),-1,-1):
    print(n)
    n = nome[0:i]