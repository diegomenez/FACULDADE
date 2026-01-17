print('='*30)
print('Calculadora de IMC')
print('='*30)
peso = float(input('Digite seu peso (kg): ')) # peso em kg
altura = float(input('Digite sua altura (m): ')) # altura em metros
imc = peso / (altura ** 2) # cálculo do IMC = peso / altura²
print('Seu IMC é {:.1f}'.format(imc)) # exibe o IMC com uma casa decimal
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')
print('='*30)
