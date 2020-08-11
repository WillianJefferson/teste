def converteHora(hora24, minuto24):
    if (hora24 > 23) or (hora24 < 0) or (minuto24 < 0) or (minuto24 > 59):
        return None
    if (hora24 < 12):
        if (hora24 == 0):
            hora24 = 12
        return 'AM', (hora24, minuto24)

    if (hora24 > 12):
        hora24 -= 12
    return 'PM', (hora24, minuto24)

# Entrada de dados
continuar = 'S'
while (continuar == 'S'):
    hora = int(input('Informe o valor da hora: '))
    minuto = int(input('Informe o valor dos minutos: '))

    print(converteHora(hora, minuto))

    continuar = input('Deseja continuar (S/N): ').upper()