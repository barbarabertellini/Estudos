totalalunos = input("Digite a quantidade total de alunos: ")
totalalunos = int(totalalunos)

homens = input("Digite a quantidade de alunos do sexo masculino: ")
homens = int(homens)

mulheres = totalalunos - homens
mulheres = (mulheres/totalalunos) * 100
homens = (homens/totalalunos) * 100

print("Alunas mulheres: ", mulheres, "%")
print("Alunos homens: ", homens, "%")