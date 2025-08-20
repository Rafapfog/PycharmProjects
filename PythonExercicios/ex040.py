n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informa a segunda nota: '))
media = (n1 + n2) / 2
print(f'A Média é: {media:.1f}')
if 10.1 > media >= 7:
    print('Aluno aprovado!')
elif 5 <= media < 7:
    print('Aluno está de recuperação.')
elif media < 5:
    print('Aluno reprovado. Procure a Direção.')
elif media > 10:
    print('Valor incorredo. Insira os valores corretos.')