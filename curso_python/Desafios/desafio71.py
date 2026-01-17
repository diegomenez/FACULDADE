print('Caixa Eletrônico')
valor = int(input('Qual valor você quer sacar? R$'))
total = valor
ced1 = 50
ced2 = 20
ced3 = 10
ced4 = 1
totalced = 0
while total >= ced1: # enquanto o total for maior ou igual a 50
    total -= ced1 # subtrai o valor da cedula do total
    totalced += 1  # conta quantas cedulas de 50 foram usadas
if totalced > 0: # se pelo menos uma cedula de 50 foi usada
    print(f'Total de {totalced} cédulas de R${ced1}') # mostra quantas cedulas de 50 foram usadas
totalced = 0 # zera o contador de cedulas
while total >= ced2:
    total -= ced2
    totalced += 1   
if totalced > 0:
    print(f'Total de {totalced} cédulas de R${ced2}')
totalced = 0
while total >= ced3:
    total -= ced3
    totalced += 1
if totalced > 0:
    print(f'Total de {totalced} cédulas de R${ced3}')
totalced = 0
while total >= ced4:
    total -= ced4
    totalced += 1   
if totalced > 0:
    print(f'Total de {totalced} cédulas de R${ced4}')
print('Volte sempre ao Caixa Eletrônico! Tenha um bom dia!')


