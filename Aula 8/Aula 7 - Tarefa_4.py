class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def engordar(self, peso):
        self.__peso += peso

    def emagrecer(self, peso):
        if (peso > self.__peso):
            self.__peso = 0
        else:
            self.__peso -= peso

    def crescer(self, altura):
        self.__altura += altura

    def envelhecer(self, anos):
        anosAntes = self.idade
        self.idade += anos
        if (anosAntes < 21):
            if (self.idade < 21):
                self.crescer(anos * 0.05)
            else:
                self.crescer((21 - anosAntes) * 0.05)


# TESTE DA CLASSE
nome = input('Informe o nome: ')
idade = int(input('Informe a idade: '))
peso = int(input('Informe o peso: '))
altura = int(input('Informe a altura: '))

lista = Pessoa(nome, idade, peso, altura)

print('engordar é igual a: ', lista.engordar())
print('emagrecer é igual a: ', lista.emagrecer())
print('crescer é igual a: ', lista.crescer())
print('envelhecer é igual a: ', lista.envelhecer())
