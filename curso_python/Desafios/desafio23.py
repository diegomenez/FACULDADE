n = int(input('digite um número de 0 a 9999: ')) # pede para o usuário digitar um número inteiro
u = n // 1 % 10 # n // 1 pega o número inteiro e % 10 pega o resto da divisão por 10
d = n // 10 % 10 # n // 10 pega o número inteiro dividido por 10 e % 10 pega o resto da divisão por 10
c = n // 100 % 10 # n // 100 pega o número inteiro dividido por 100 e % 10 pega o resto da divisão por 10
m = n // 1000 % 10 # n // 1000 pega o número inteiro dividido por 1000 e % 10 pega o resto da divisão por 10
print('analisando o número {}'.format(n))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c)) 
print('milhar: {}'.format(m))

# + adição
# - subtração
# * multiplicação
# / divisão
# // divisão inteira
# % resto da divisão
# ** potência
# () prioridade
# ordem de precedência: 1°() 2°** 3°* / // % 4°+ -
# para fazer raiz quadrada use potência com 1/2
# exemplo: n**(1/2)
# para fazer raiz cúbica use potência com 1/3
# exemplo: n**(1/3)
# para fazer arredondamento para cima use a função math.ceil()
# para fazer arredondamento para baixo use a função math.floor()
# para fazer arredondamento normal use a função round()