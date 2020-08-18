def mes_extenso( data_str ):
    if len(data_str) != 10 :
        return NULL # data em formato invalido
    data_str= data_str.split('/')
    if len(data_str) != 3 :
        return NULL # data em formato invalido
    meses =['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

    dia = data_str[0]
    mes = meses[int(data_str[1])-1]
    ano = data_str[2]

    extenso = dia+" de "+mes+" de "+ano
    return extenso

print( mes_extenso('01/01/2021'))