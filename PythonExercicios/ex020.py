# o mesmo professor do desafio anterios quer sortear a ordem de apresentacao de trabalhos dos alunos,
# faça um programa que leia o nome dos quarto alunos e mostre a irdem sorteada
import random
n1 = str(input('informe o nome do primeiro aluno: ')).strip()
n2 = str(input('Informe o nome do segundo aluno: ')).strip()
n3 = str(input('Informe o nome do terceiro aluno: ')).strip()
n4 = str(input('Informe o nome do terceiro aluno: ')).strip()
alunos = [n1, n2, n3, n4]
random.shuffle(alunos)
print(f'O aluno escolhido foi o {alunos}.')