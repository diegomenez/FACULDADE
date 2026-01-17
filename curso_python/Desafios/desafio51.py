print('Descubra se um número é primo ou não')
n = int(input('Digite um número: '))

# Números 0 e 1 não são primos por definição
if n <= 1:
    eh_primo = False
else:
    eh_primo = True  # Assume que é primo até provar o contrário
    
    # Testa todos os divisores de 2 até (n-1)
    for c in range(2, n):
        # O operador % (módulo) calcula o RESTO da divisão
        if n % c == 0:
            # Se o resto for 0, encontramos um divisor!
            # Logo, o número NÃO é primo.
            eh_primo = False
            break  # Já sabemos que não é primo, podemos parar o loop

# Exibe o resultado final
if eh_primo:
    print(f'O número {n} é primo!')
else:
    print(f'O número {n} não é primo!')