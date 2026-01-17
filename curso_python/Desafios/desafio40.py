print('Bem-vindo Aluno! Vamos calcular sua média final.')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Sua média foi {:.1f}. Você está REPROVADO.'.format(media))
elif 5.0 <= media < 6.9:
    print('Sua média foi {:.1f}. Você está de RECUPERAÇÃO.'.format(media))
else:
    print('Sua média foi {:.1f}. PARABÉNS! Você está APROVADO.'.format(media))
    