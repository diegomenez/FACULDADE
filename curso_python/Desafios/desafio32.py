a = int(input("Digite o ano que queira verificar se é bissexto: "))  # Lê o ano do usuário
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0): # Verifica se o ano é bissexto
    print("O ano {} é bissexto.".format(a))  # Mensagem para ano bissexto
else:
    print("O ano {} não é bissexto.".format(a))  # Mensagem para ano não bissexto   
    