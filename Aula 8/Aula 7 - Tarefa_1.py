class Bola:

    def __init__(self, cor, circunferencia, material):
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material

    def trocar_cor(self):
        self.__cor = cor

    def mostra_cor(self):
        return self.__cor

bola_futebol = Bola('branca', 3.5 ,'couro')

print(bola_futebol.mostra_cor())