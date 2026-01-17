nome = input('digite seu nome: ').strip() #strip() remove espaços extras no início e no fim
print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é assim: {}'.format(nome.upper())) #upper() converte todas as letras para maiúsculas
print('Seu nome em letras minúsculas é assim: {} '.format(nome.lower())) #lower() converte todas as letras para minúsculas
print('Seu nome tem {} letras'.format(len(nome.replace(' ', '')))) #replace() remove os espaços entre os nomes para contar apenas as letras
print('Seu primeiro nome é {} e tem {} letras'.format(nome.split()[0], len(nome.split()[0]))) #split() divide o nome em partes e [0] pega a primeira parte (primeiro nome)


