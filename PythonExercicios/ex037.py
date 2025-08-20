numero = int(input('Digite um numero inteiro: '))
print('''DIgite um valor para conversão:
[1] para binário,
[2] para octal
[3] para hexadecimal''')
opcao = int(input('Qual sua opção: '))
if opcao == 1:
    print(f'{numero} convertido para binário é igual a {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{numero} convertido para octal é igual a {oct(numero)[2:]}')
elif opcao == 3:
    print(f'{numero} convertido para hexadecimal é igual a {hex(numero)[2:]}')
else:
    print('Opção inválida, tente novamente. Obrigado!!!')
