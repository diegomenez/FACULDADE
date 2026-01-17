nome = input('Digite seu nome completo: ').strip().split() # .strip() remove espaços extras no início e no fim, .split() divide o nome em partes
print('Seu primeiro nome é {}'.format(nome[0])) # Acessa o primeiro elemento da lista
print('Seu último nome é {}'.format(nome[-1])) # Acessa o último elemento da lista usando índice negativo