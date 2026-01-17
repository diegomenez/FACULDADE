print('bem vindo ao conversor de unidades')
n = int(input('Digite um valor para realizar a conversão: '))
f = input('digite 1 para binário, 2 para octal e 3 para hexadecimal :')
if f == '1':
    print('{} convertido para binário é igual a {}'.format(n, bin(n)[2:]))
elif f == '2':
    print('{} convertido para octal é igual a {}'.format(n, oct(n)[2:]))
elif f == '3':
    print('{} convertido para hexadecimal é igual a {}'.format(n, hex(n)[2:]))

else:
    print('opção inválida, tente novamente')