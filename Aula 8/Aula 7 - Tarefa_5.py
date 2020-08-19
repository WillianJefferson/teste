class ContaCorrente:

    def __init__(self, numero, nomeCorrentista, saldo=0.0):
        self.numero = numero
        self.alterar_nome(nomeCorrentista)
        self.saldo = saldo

    def alterar_nome(self, nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor



nome = input('Informe o nome: ')

conta = ContaCorrente(10000, 'Willian')
conta.deposito(100)
print(conta.saldo)
conta.saque(200)
print(conta.saldo)
