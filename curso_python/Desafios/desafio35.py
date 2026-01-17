print ( 'Vamos ver se as 3 retas podem formar um triângulo!' )  # Instrução inicial para o usuário
r1 = float ( input ( 'Digite primeiro o comprimento da maior reta: ' ) )  # Lê o comprimento da primeira reta
r2 = float ( input ( 'Digite o comprimento da segunda reta: ' ) )  # Lê o comprimento da segunda reta
r3 = float ( input ( 'Digite o comprimento da terceira reta: ' ) )  # Lê o comprimento da terceira reta
if r1 < r2 + r3 :  # Verifica a condição para formar um triângulo
    print ( 'As retas podem formar um triângulo!' )  # Mensagem de sucesso  
else :
    print ( 'As retas não podem formar um triângulo!' )  # Mensagem de falha
    
