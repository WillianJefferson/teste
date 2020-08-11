def qt_digito( numero ) :
    numero_str = str(numero)
    return( len(numero_str))

numero = int (input("Entre com um numero: "))
print( "Quantidade de digitos do número ", numero, " - digitos: ", qt_digito(numero))