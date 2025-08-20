# faça um programa que informe seu primeiro e ultimo nome:

nome = str(input('Digite seu nome completo: ')).strip()
no = nome.split()
print(f'Prazer em te conhecer {nome}!')
print(f'Seu primeiro nome é {no[0]}')
print(f'Seu último nome é {no[-1]}')
print(no)
