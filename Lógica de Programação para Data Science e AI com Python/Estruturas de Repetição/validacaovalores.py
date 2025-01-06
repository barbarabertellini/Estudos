val1 = int(input("Digite o primeiro valor: "))
val2 = int(input("Digite o segundo valor: "))

if val1>10 or (val2 < val1 * 10):
        print("Valor inválido")
while val1<10 and (val2 >= val1 * 10):
    print(val1 * val2)
    break

