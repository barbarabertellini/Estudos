num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número, esse deve ser maior que o primeiro: "))

if num1 >= 0 and num2 >= 0: 
    if num1 < num2: 
        print("Ordem crescente:")
        for i in range(num1, num2 + 1):
            print(i, end=" ")

        print("\nOrdem decrescente:")
        for i in range(num2, num1 - 1, -1):
            print(i, end=" ")
    else:
        print("Erro: O segundo número deve ser maior que o primeiro.")
else:
    print("Erro: Ambos os números devem ser positivos.")
