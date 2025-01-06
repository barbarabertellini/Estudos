nota = float(input("Digite a nota do aluno: "))

if nota>=7:
    print("Aprovado!")
else:
    notaexame = float(input("Digite a nota do exame: "))
    total = nota + notaexame
    if (total/2)<6:
        print("Reprovado")
    else: 
        print("Aprovado")