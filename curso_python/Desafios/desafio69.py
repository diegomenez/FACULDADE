print(('<'*5),('Cadastro de Pessoas'),('>'*5))
maior = 0
menor = 0
s = 0
m = 0
f = 0
while True:
    idade = int(input('Digite a idade: '))
    s += idade
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        maior += 1
        m += 1
    elif sexo == 'F' and idade < 20:
        menor += 1
        f += 1
    elif sexo == 'F'and idade >= 20:
        f += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Total de homens cadastrados: {m}')
print(f'Total de mulheres com menos de 20 anos: {menor}')
print(f'Total de mulheres cadastradas: {f}')