nota_1 = 0
nota_2 = 0
media = 0

nota_1 = float(input("Informe a primeira nota : "))
nota_2 = float(input("Informe a segunda nota : "))

media = (nota_1 + nota_2) / 2.0

print("Media alcançada : ", media)
if (media == 10):
    print("Aprovado com Distinção")
elif (media >= 7):
    print("Aprovado")
else:
    print("Reprovado")