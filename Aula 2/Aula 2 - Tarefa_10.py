turno = ""

print("-- Em que turno voce estuda?")
print("-- Digite M para matutino, V para vespertino ou N para noturno")

turno = input("Opção escolhida: ").upper()

if (turno == "M"):
    print("Bom dia!")
elif (turno == 'V'):
    print("Boa tarde!")
elif (turno == 'N'):
    print("Boa noite!")
else:
    print("Valor invalido")