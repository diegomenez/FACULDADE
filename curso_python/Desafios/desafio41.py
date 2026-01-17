from datetime import date # Importa a biblioteca date do módulo datetime para trabalhar com datas
print("") # Imprime uma linha em branco para melhor formatação
print('BEM VINDO a C.N.N. Confederação Nacional de Natação') # Mensagem de boas-vindas
print("")
ano = int(input('Digite o ano de nascimento do atleta: ')) # Solicita ao usuário o ano de nascimento do atleta e converte para inteiro
idade = date.today().year - ano # Calcula a idade do atleta subtraindo o ano de nascimento do ano atual
print('O atleta tem {} anos.'.format(idade)) # Exibe a idade do atleta
if idade <= 9: 
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 20:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
