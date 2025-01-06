from statistics import mean

lista = list(range(1,11))

for n in range(0, 10):
    print("Informe o número da posição ", n+1)
    lista[n] = int(input())
    while lista[n] <=0:
        print("Entrada Inválida, por favor repita!")
        lista[n] = int(input())


soma = 0
for n in range(0, 10):
    soma += lista[n]

print("Média calculada \"manualmente\" igual a: ", soma / 10)    


print("Média calculada \"por função\" igual a: ",mean(lista))
