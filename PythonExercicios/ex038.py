num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informa o segundo número: '))
print(f'voce escolheu os numeros {num1} e {num2}.')
if num1 > num2:
    print(f'E o primeiro é o maior ({num1})')
elif num1 < num2:
    print(f'e o número maior é o segundo ({num2}).')
else:
    print('E os dois números sao iguais.')
