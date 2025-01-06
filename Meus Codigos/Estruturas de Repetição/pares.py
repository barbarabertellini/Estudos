entrada = 5
qtdvalores = 0
soma = 0
produto = 1

for n in range(1, entrada+1):
    n = int(input("Digite o " +str(n)+ " valor: "))
    if n%2==0:
        qtdvalores = qtdvalores + 1
        soma = soma + n
        produto = produto * n

print ("A quantidade de valores pares é ", qtdvalores)
print ("A soma dos valores pares é ", soma)
print ("O produto dos valores pares é ", produto)