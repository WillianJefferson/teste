num = 0
ite = 0
mai = 0

for i in range(0, 5):
    num = int(input("Informe um número: "))
    if ("maior" in vars()):
        if (num > mai):
            mai = num
    else:
        mai = num

print("O maior número que você digitou é : ", mai)