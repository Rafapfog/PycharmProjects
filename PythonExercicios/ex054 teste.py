from datetime import date
menores = 0
for c in range(1, 8):
    pessoa = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if date.today().year - pessoa < 21:
        menores += 1
print(f'\n{7 - menores} são Maiores e {menores} são menores.')