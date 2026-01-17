frase = input('Digite uma frase: ').strip().upper() # pega a frase, remove espaços desnecessários e converte para maiúsculas
print('A letra A aparece {} vezes na frase'.format(frase.count('A'))) # conta quantas vezes a letra A aparece na frase
print('A letra A aparece na posição {}' .format(frase.find('A'))) # mostra a posição da primeira letra A
print('A letra A aparece pela ultima vez na posição {}'.format(frase.rfind('A'))) # mostra a posição da última letra A
