print('<'*8,'Loja do Menezes','>'*8)
total = 0
mais1000 = 0
menorpreco = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        mais1000 += 1
    if menorpreco == 0 or preco < menorpreco:
        menorpreco = preco
        prodmenor = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {prodmenor} que custa R${menorpreco:.2f}')

