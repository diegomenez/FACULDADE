class Conta:
    def __init__(self, cliente, numero, saldo):
        self.cliente = cliente
        self.numero = numero      
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        else:
            print("Saldo insuficiente para saque.")
    
    def tranfere_valor(self, conta_destino, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(f'Transferência de R$ {valor:.2f} para a conta {conta_destino.numero} realizada com sucesso.')
        else:
            print("Saldo insuficiente para transferência.")

    def gerar_saldo(self):
        print(f'Saldo da conta {self.numero}: R$ {self.saldo:.2f}')