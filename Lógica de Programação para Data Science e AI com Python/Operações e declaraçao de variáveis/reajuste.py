salario = input("Digite o salário do funcionário: ")
salario = float(salario)

reajuste = input("Digite o percentual do reajuste do salário: ")
reajuste = float(reajuste)

total = (salario * reajuste) + salario

print("O salário após o reajuste é de", total, "reais")