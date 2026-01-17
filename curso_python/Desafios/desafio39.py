from datetime import date
print('Bem vindo ao Exercito Brasileiro!')
i = int(input('Digite sua idade: '))
if i < 16:
    print('Você ainda não tem idade para se alistar.')
elif i == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
    print('Procure o posto de alistamento mais próximo até o final do ano.')
elif i > 18:
    a = i - 18
    ano = date.today().year - a
    print('Você já deveria ter se alistado há {} anos.'.format(a))
    print('Seu alistamento foi em {}.'.format(ano))
else:
    a = 18 - i
    ano = date.today().year + a
    print('Ainda faltam {} anos para o seu alistamento.'.format(a))
    print('Seu alistamento será em {}.'.format(ano))