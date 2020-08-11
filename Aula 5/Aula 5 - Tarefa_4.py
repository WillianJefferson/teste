def positivo_negativo ( numero ):
    if numero >0 :
        return ('P')
    else:
        return ('N')

numero = int(input("Entre com um numero inteiro: "))
print(positivo_negativo( numero ))