idade = int(input("Informe a idade: "))
nota = float(input("Informa a nota: "))
brasileiro = input("Digite \"S\" se é brasileiro ou \"N\" caso não seja: ")
brasileiro = brasileiro.upper()

if idade<25 and nota>=70 and brasileiro=="S":
    print("Aprovado!")
else:
    print("Reprovado!")