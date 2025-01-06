valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor1==valor2:
    print("São iguais")
elif valor1!=valor2:
    if valor1>valor2:
        print("São diferentes e o primeiro valor é o maior")
    else: 
        print("São diferentes e o segundo valor é o maior")
