# um professor quer sortear um dos seus alunos para apagar o quadro. faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome escolhido.
import random
n1 = str(input('informe o nome do primeiro aluno: ')).strip()
n2 = str(input('Informe o nome do segundo aluno: ')).strip()
n3 = str(input('Informe o nome do terceiro aluno: ')).strip()
n4 = str(input('Informe o nome do terceiro aluno: ')).strip()
alunos = [n1,n2,n3,n4]
aluno = random.choice(alunos)
print(f'O aluno escolhido foi o {aluno}.')