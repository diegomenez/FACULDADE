nome = input('Digite seu nome completo: ').strip() #pega o nome completo e remove espaços desnecessários
nome = nome.upper() #converte o nome para maiúsculas
print('Seu nome tem Silva? {}'.format('SILVA' in nome)) #verifica se 'SILVA' está no nome e imprime o resultado