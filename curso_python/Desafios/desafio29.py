print("Você acabou de passar por um radar de velocidade!")  # Instrução inicial para o usuário
v = float(input("Digite a velocidade do seu carro em km/h: "))  # Lê a velocidade do carro
if v > 80:
    multa = (v - 80) * 7  # Calcula o valor da multa
    print("Você foi multado! O limite de velocidade da rodovia era de 80km/h. O valor da multa é R$ {:.2f}".format(multa))  # Exibe o valor da multa
else:
    print("Parabéns! Você está dentro do limite de velocidade.")  # Mensagem de conformidade com o limite