from Cliente import Cliente
from Conta import Conta


cliente1 = Cliente('Diego', '123.456.789-00', 'Rua X')    
cliente2 = Cliente('Ana', '987.654.321-00', 'Avenida Y')

conta1 = Conta(cliente= [cliente1, cliente2], numero='111', saldo= 0)

print('---' * 10)
print('Banco Python')
print(f'Bem vindo, {cliente1.nome}!')
print(f'Seu saldo atual é de R$ {conta1.saldo:.2f}')
print('---' * 10)
print('Operações disponíveis:')
print('1 - Depositar')
print('2 - Sacar')
print('3 - Transferir')
inicio = int(input('Qual operação deseja realizar? '))
if inicio == 1:
    conta1.depositar(int(input('Qual valor deseja depositar? ')))
elif inicio == 2:
        conta1.sacar(int(input('Qual valor deseja sacar? ')))
elif inicio == 3:
        conta2 = Conta(cliente= cliente2, numero='222', saldo= 0)
        conta1.tranfere_valor(conta2, int(input('Qual valor deseja transferir? ')))
else:
    print('Operação inválida.')
    
conta1.gerar_saldo()

