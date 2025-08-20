#analisar o nome da pessoa sem contar os espaços>
#mostrar o nome em letras maiusculas;
#mostrar em letras minusculas;
#quantas letras tem o primeiro nome

nome = str(input('Informe o seu nome: ')).strip()
print(f'Seu nome maiusculo é: {nome.upper()}')
print(f'Seu nome minusculo é: {nome.lower()}')
print(f'Seu nome Capitalizado é: {nome.capitalize()}')
print(f'Seu nome titulado é: {nome.title()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras.')
print(f'Seu primeiro nome tem {nome.find(' ')} letras.')
separa = nome.split()
print(f'Seu primeiro nome tem {len(separa[0])} letras.')