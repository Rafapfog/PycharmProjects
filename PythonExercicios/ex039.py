from datetime import date
nascimento = int(input('Informe seu ano de nascimento: '))
idade = date.today().year - nascimento
falta = 18 - idade
passou = idade - 18
print('idade:', idade)
if idade < 18:
    print('voce ainda nao precisa se alistar')
    print(f'Ainda falta(m) {falta} ano(s).')
elif idade == 18:
    print('Voce está no ano de se alistar! Corra!!!')
elif idade > 18:
    print(f'''Voce já passou {passou} anos da idade para se alistar!
Corra a uma junta militar para regularizar sua pendencia!''')