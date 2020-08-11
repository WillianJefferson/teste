def reverso(numero):
    numero_str = str(numero)
    inverso = ""

    for i in range(len(numero_str)-1,-1,-1):
        inverso += numero_str[i]

    return(int(inverso))

numero = int(input("Entre com um número: "))
print("Número: ", numero, " - Invertido: ", reverso(numero))