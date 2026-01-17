# tabuada usando laço de repetição
n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11): #loop de 1 a 10
    print(f'{n} x {c} = {n * c}')  #mostra o resultado da multiplicação (o "f" antes da string indica que é uma f-string, permitindo a inclusão de expressões dentro das chaves)