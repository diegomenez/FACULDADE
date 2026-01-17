print('soma de numeros impares multiplos de 3 entre 1 e 500')
s = 0 #variável para armazenar a soma
for c in range(1, 501, 2): #loop para números ímpares de 1 a 500
    if c % 3 == 0: #verifica se o número é múltiplo de 3
        s += c #adiciona o número à soma
print('O resultado é:', s) #mostra o resultado final