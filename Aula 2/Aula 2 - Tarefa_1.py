n1 = 0
n2 = 0

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))

if (n1 > n2):
    print (n1, "É maior que : ", n2)
elif (n1 < n2):
    print (n2, 'É maior que : ', n1)
else:
    print ("Os números são iguais")