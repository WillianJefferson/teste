lista_completa = []

for i in range(0, 5):
    dados = []
    dados.append(input('Informe a idade da pessoa: '))
    dados.append(input('Informe a altura da pessoa: '))
    lista_completa.append(dados)

lista_completa.reverse()
print("")
for dados in lista_completa:
    print("Idade: ", dados[0], " Altura: ", dados[1])