var1 = input("Digite um numero: ")
var1 = str(var1)

var2 = input("Digite outro numero: ")
var2 = str(var2)

temp = var1
var1 = var2
var2 = temp

print("Invertendo os números, o primeiro número é: ", var1)
print("Invertendo os números, o segundo1 número é: ", var2)