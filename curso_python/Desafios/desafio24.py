cidade = input('Em que cidade você nasceu? ').strip() #remove espaços em branco antes e depois
cidade = cidade.split() #divide a string em uma lista
print('santo' == cidade[0].lower()) #verifica se o primeiro elemento da lista é igual a 'santo' ignorando maiúsculas e minúsculas
