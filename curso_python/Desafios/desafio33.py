print('Vamos descobrir qual é o maior e o menor número entre 3 números!')  # Instrução inicial para o usuário
n1 = float(input('Digite o primeiro número: '))  # Lê o primeiro número
n2 = float(input('Digite o segundo número: '))   # Lê o segundo número
n3 = float(input('Digite o terceiro número: '))  # Lê o terceiro número
if n1 >= n2 and n1 >= n3:
    maior = n1  # Define o maior número como n1 
elif n2 >= n1 and n2 >= n3:
    maior = n2  # Define o maior número como n2     
else:
    maior = n3  # Define o maior número como n3
print('O maior número entre {}, {} e {} é: {}'.format(n1, n2, n3, maior))  # Exibe o maior número
if n1 <= n2 and n1 <= n3:
    menor = n1  # Define o menor número como n1 
elif n2 <= n1 and n2 <= n3:
    menor = n2  # Define o menor número como n2
else:       
    menor = n3  # Define o menor número como n3
print('O menor número entre {}, {} e {} é: {}'.format(n1, n2, n3, menor))  # Exibe o menor número
