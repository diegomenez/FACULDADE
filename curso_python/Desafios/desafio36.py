valor = int(input('Informe o valor da casa: R$ '))
salario = float(input('Informe o salário do comprador: R$ '))
anos = int(input('Informe em quantos anos o empréstimo será pago: '))
prestacao = valor / (anos * 12)
if prestacao > (salario * 0.3):
    print('Empréstimo negado! A prestação mensal de R$ {:.2f} excede 30% do salário.'.format(prestacao))
else:
    print('Empréstimo aprovado! A prestação mensal será de R$ {:.2f}.'.format(prestacao))