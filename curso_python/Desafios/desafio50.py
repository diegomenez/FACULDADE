print('Digite 6 numeros inteiros e veja a soma dos pares')
s = 0 #variável para armazenar a soma
for c in range(1, 7): #loop de 1 a 6
    n = int(input(f'Digite o {c}º número: ')) #solicita ao usuário que digite um número
    if n % 2 == 0: #verifica se o número é par
        s += n #adiciona o número à soma
print('A soma dos números pares é:', s) #mostra o resultado final1

    