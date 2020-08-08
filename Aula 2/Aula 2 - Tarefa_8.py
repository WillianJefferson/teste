preco_1 = 0
preco_2 = 0
preco_3 = 0

preco_1 = int(input("Informe o primeiro preço: "))
preco_2 = int(input("Informe o segundo preço: "))
preco_3 = int(input("Informe o terceiro preço: "))

if (preco_1 == preco_2) and (preco_1 == preco_3):
    print("Pode comprar qualquer um, ja que os precos sao iguais.")
elif (preco_1 < preco_2) and (preco_1 < preco_3):
    print("")
    print("Compre pelo primeiro preço")
elif (preco_2 < preco_3):
    print("")
    print("Compre pelo segundo preço")
else:
    print("")
    print("Compre pelo terceiro preço")