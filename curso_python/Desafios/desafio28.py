from random import randint
print("Adivinhe o número que estou pensando entre 1 e 10!")  # Instrução inicial para o usuário
n1 = int(input("Digite um número: "))          # Lê um número inteiro do usuário
n2 = randint (1,10)  # Gera um número aleatório entre 1 e 10
if n1 == n2: # Verifica se o número do usuário é igual ao número gerado
    print("Parabéns! Você adivinhou o número!")  # Mensagem de sucesso
else:
    print("Que pena! O número correto era", n2)  # Mensagem de falha com o número correto
    