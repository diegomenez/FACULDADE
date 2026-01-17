n1 = float(input("Digite a primeira nota: ")) # Lê a primeira nota do usuário
n2 = float(input("Digite a segunda nota: ")) # Lê a segunda nota do usuário
media = (n1 + n2) / 2  # Calcula a média das notas
print("A média é:", media) # Exibe a média calculada
if media >= 6: # Verifica se a média é maior ou igual a 6
    print("Parabens, você foi aprovado!") # Mensagem de aprovação
else: # Caso a média seja menor que 6
    print("Você foi reprovado. Tente novamente!") # Mensagem de reprovação
