def somaimposto (imposto, custo):

    valor_imposto = custo * imposto
    valor = custo + valor_imposto
    return(valor)

custo = float(input( "Entre valor do custo do produto: "))
imposto=float(input( "Entre com a taxa de imposto (decimal ): "))

valor = somaimposto( imposto, custo)

print("Custo:", custo, " perc imposto :", imposto, " valor após imposto: ", valor)