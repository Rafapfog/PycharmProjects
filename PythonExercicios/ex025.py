# fazer um programa que verifique se tem o nome silva no nome em qualquer lugar.
nome = str(input('Qual seu nome completo: ')).strip()
print(f'Seu nome completo é {nome}')
print(f"tem Silva no seu nome? {'Silva' in nome.title()}")
