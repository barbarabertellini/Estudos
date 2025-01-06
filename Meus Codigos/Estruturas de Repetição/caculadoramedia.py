qtd = int(input("Digite a quantidade de números que você quer calcular a média: "))
soma = 0

for qtd in range(1, qtd +1):
    texto = "Informe o " +str(qtd)+ " número: "
    soma = soma + float(input(texto))

print("A média é igual a: ", soma/qtd)

