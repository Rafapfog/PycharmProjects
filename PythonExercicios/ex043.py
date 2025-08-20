peso = float(input('Qual é seu peso: (Kg)'))
altura = float(input('Qual é sua altura: (m)'))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Voce está Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Voce está no Peso Ideal, parabéns!')
elif 25 <= imc < 30:
    print('Voce está com Sobrepeso.')
elif 30 <= imc < 40:
    print('Voce está com Obesidade!')
elif imc >= 40:
    print('Você está com Obesidade Morbida. Cuidado!')
else:
    print('Informações incorretas, tente novamente!')