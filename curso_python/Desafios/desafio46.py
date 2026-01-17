print('Contagem regressiva para o estouro de fogos!')
from time import sleep #importa a função sleep do módulo time
for c in range(10, -1, -1): #contagem regressiva de 10 até 0
    print(c) #mostra o número atual da contagem
    sleep(1) #pausa o programa por 1 segundo    
print('FELIZ ANO NOVO!!!') #mensagem final após a contagem
