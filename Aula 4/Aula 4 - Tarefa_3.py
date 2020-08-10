vetor_notas = []
total = 0
media = 0

for i in range(0, 4):
    vetor_notas.append(float(input("Digite uma nota: ")))

print("\n Notas Digitadas: ")

for i in range(0, 4):
    print("Nota ", i, ": ", vetor_notas[i])
    total = total + vetor_notas[i]

media = total / 4

print("Média das notas: ", media)
