def valor_pagamento(valor, dias_a):

    if (valor < 0):
        return None
    if (dias_a > 0):
        multa = valor * 0.03
        adicional = valor * (dias_a * 0.01)
        return valor + multa + adicional
    else:
        return valor

valor = 1
while (valor != 0):
    valor = float(input('Informe o valor da prestação: '))
    if (valor != 0):
        dias_a = int(input('Informe a quantidade de dias de atraso: '))
        print("Valor a ser pago: ", valor_pagamento(valor, dias_a))
