inicial = 0
final = 0
i = 0

inicial = int(input("Digite o valor inicial: "))
final = inicial
while (final <= inicial):
    final = int(input("Digite o valor final: "))
    if (final <= inicial):
        print("O valor final deve ser maior que o inicial")

inicial = inicial + 1
final = final - 1

print("")

for i in range(inicial, final + 1):
    print(i)