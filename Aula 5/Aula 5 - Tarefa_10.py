import random

# Função para Jogar os Dados
def jogar_dados():
    jogada = random.randint(2, 12)
    return jogada

quant = 1
termina = False
ponto = 0

while (not termina):
    jogada = jogar_dados()
    print("Jogada : ", (quant, jogada))

    if (quant == 1):
        if (jogada == 2) or (jogada == 3) or (jogada == 12):
            print(f"Craps! Voce Perdeu!")
            termina = True
        elif (jogada == 7) or (jogada == 11):
            print("Voce é natural e Ganhou! ")
            termina = True
        else:
            ponto = jogada
            print("Seus pontos : ", ponto)
    else:
        if (jogada == 7):
            print("Voce Perdeu!")
            termina = True
        elif (jogada == ponto):
            print("Voce Ganhou!")
            termina = True
    quant += 1
