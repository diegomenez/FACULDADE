class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf      
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor   

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        else:
            print("Saldo insuficiente para saque.")

    def transferir(self, valor, contaDestino):
        if valor <= self.saldo:
            self.saldo -= valor
            contaDestino.depositar(valor)
            print(f'Transferência de R$ {valor:.2f} para a conta {contaDestino.numero} realizada com sucesso.')
        else:
            print("Saldo insuficiente para transferência.")
c1 = Conta(numero=1, cpf="123.456.789-00", nomeTitular="Diego Menezes", saldo=1000.0)
c2 = Conta(numero=2, cpf="987.654.321-00", nomeTitular="Ana Silva", saldo=500.0)
#c1.depositar(500)
#c1.sacar(200)
c1.transferir(300, c2)
print(f'Nome do titular da conta: {c1.nomeTitular}')
print(f'Número da conta: {c1.numero}')
print(f'Saldo da conta: R$ {c1.saldo:.2f}')
