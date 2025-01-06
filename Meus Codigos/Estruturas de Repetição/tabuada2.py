num = int(input("Você quer imprimir a tabuada de qual número? "))

for n in range(1,11):
    print(n, "x", num, "=", n*num)

outra = int(input("Quer imprimir outra tabuada? Digite 1 para prosseguir e 2 para encerrar: "))
while outra==1:
    num = int(input("Você quer imprimir a tabuada de qual número? "))
    for n in range(1,11):
        print(n, "x", num, "=", n*num)
    outra = int(input("Quer imprimir outra tabuada? Digite 1 para prosseguir e 2 para encerrar: "))
if outra==2:
    print("Sistema finalizado")
