d = float(input("Digite a distância da viagem em km: "))  # Lê a distância da viagem
if d <= 200:
    preço = d * 0.50  # Calcula o preço para viagens até 200 km
else:
    preço = d * 0.45  # Calcula o preço para viagens acima de 200 km
print("O preço da passagem é R$ {:.2f}".format(preço))  # Exibe o preço da passagem
