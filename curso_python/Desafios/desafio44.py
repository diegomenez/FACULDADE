print('==' * 30)
print('Calculadora de preços')
preco = float(input('Digite o preço do produto: R$ ')) # Recebe o preço do produto
print('''Escolha a forma de pagamento:                 ## Menu de opções
[ 1 ] à vista dinheiro/cheque   (10% de desconto)
[ 2 ] à vista no cartão         (5% de desconto)            
[ 3 ] em até 2x no cartão       (preço normal)
[ 4 ] 3x ou mais no cartão      (20% de juros)''') # Exibe as opções de pagamento
opcao = int(input('Qual é a opção? ')) # Recebe a opção escolhida
if opcao == 1:
    total = preco - (preco * 10 / 100) # Calcula o preço com 10% de desconto
    print(f'Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} no final.') # Exibe o preço final    
elif opcao == 2:
    total = preco - (preco * 5 / 100) # Calcula o preço com 5% de desconto
    print(f'Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} no final.') # Exibe o preço final
elif opcao == 3:
    total = preco # Preço normal
    parcela = total / 2 # Divide o preço em 2 parcelas
    print(f'Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} no final.') # Exibe o preço final
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f} sem juros.') # Exibe o valor das parcelas
elif opcao == 4:
    total = preco + (preco * 20 / 100) # Calcula o preço com 20% de juros
    total_parcelas = int(input('Quantas parcelas? ')) # Recebe o número de parcelas
    parcela = total / total_parcelas # Divide o preço em parcelas
    print(f'Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} no final.') # Exibe o preço final
    print(f'Sua compra será parcelada em {total_parcelas}x de R$ {parcela:.2f} com juros.') # Exibe o valor das parcelas