print ( 'Vamos ver se as 3 retas podem formar um triângulo!' )  # Instrução inicial para o usuário
r1 = float ( input ( 'Digite primeiro o comprimento da maior reta: ' ) )  # Lê o comprimento da primeira reta
r2 = float ( input ( 'Digite o comprimento da segunda reta: ' ) )  # Lê o comprimento da segunda reta
r3 = float ( input ( 'Digite o comprimento da terceira reta: ' ) )  # Lê o comprimento da terceira reta
if r1 == r2 == r3 :
    print ( 'As retas podem formar um triângulo EQUILÁTERO!' )  # Mensagem de triângulo equilátero
elif r1 != r2 != r3 != r1 :
    print ( 'As retas podem formar um triângulo ESCALENO!' )  # Mensagem de triângulo escaleno
elif r1 < r2 + r3 :
    print ( 'As retas podem formar um triângulo ISÓSCELES!' )  # Mensagem de triângulo isósceles
else :
    print ( 'As retas não podem formar um triângulo!' )  # Mensagem de falha
