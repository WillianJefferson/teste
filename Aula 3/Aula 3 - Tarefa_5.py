pop_A = input("digite a populacao A ---> ")
pop_B = input("digite a populacao B ---> ")
cre_A = input("digite a taxa de crescimento população A (ex: 0.1 para 10% ---> ")
cre_B = input("digite a taxa de crescimento população B (ex: 0.1 para 10% ---> ")

pop_A = 80000
cre_A = 1.03
pop_B = 200000
cre_B = 1.015

# Calculo de anos necessarios ate A utrapassar B
ano = 1
while (pop_A <= pop_B):
    pop_A *= cre_A
    pop_B *= cre_B
    ano += 1

# Imprime o resultado
print("Serão necessarios", ano )
print("Para que a população do pais A ultrapasse a populacao do pais B")