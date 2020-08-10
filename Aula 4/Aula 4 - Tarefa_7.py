numeros = []
soma = 0
mult = 1

for i in range(0, 5):
    numeros.append(int(input("Digite um número inteiro: ")))

for i in numeros:
    soma += i
    mult *= i

print("")
print(numeros)
print("Soma dos numeros: ", soma)
print("Multiplicacao dos numeros: ", mult)