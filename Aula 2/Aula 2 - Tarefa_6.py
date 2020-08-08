n1 = 0
n2 = 0
n3 = 0

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

if (n1 == n2) and (n1 == n3):
    print("Os números são iguais")
elif (n1 > n2) and (n1 > n3):
    print(n1, " É o maior número")
elif (n2 > n3):
    print(n2, " É o maior número")
else:
    print(n3, " É o maior número")