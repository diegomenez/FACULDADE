print("Vamos descobrir seu novo salario para o ano que vem!")  # Instrução inicial para o usuário
s = float(input("Digite o salário atual do funcionário: R$ "))  # Lê o salário atual
if s <= 1250:
    ns = s + (s * 0.10)  # Calcula o novo salário com aumento de 10%
else:
    ns = s + (s * 0.15)  # Calcula o novo salário com aumento de 15%
print("O novo salário do funcionário será: R$ {:.2f}".format(ns))  # Exibe o novo salário
