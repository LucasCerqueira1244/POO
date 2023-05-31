class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")


class ContaCorrente(Conta):
    def sacar(self, valor):
        taxa = 1.05  # Taxa de saque para conta corrente
        valor_com_taxa = valor * taxa
        if self.saldo >= valor_com_taxa:
            self.saldo -= valor_com_taxa
        else:
            print("Saldo insuficiente.")


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")


conta1 = ContaCorrente(1000)
conta2 = ContaPoupanca(2000)

conta1.sacar(500)  # Chama o método "sacar" da classe ContaCorrente
conta2.sacar(300)  # Chama o método "sacar" da classe ContaPoupanca

print(conta1.saldo)  # Exibe o saldo atual da conta1
print(conta2.saldo)  # Exibe o saldo atual da conta2