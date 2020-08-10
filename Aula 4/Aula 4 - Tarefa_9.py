a = []
for i in range(0, 10):
    a.append(int(input("Digite um número: ")))

soma = 0
for n in a:
    soma += (n * n)

print("A soma dos quadrados = ", soma)