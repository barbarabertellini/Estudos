quantidade = int(input("Digite a quantidade de produtos comprados: "))
valortotal = float(input("Digite o valor total da compra: "))
print("O valor da compra foi",valortotal)

if quantidade==2:
    print("O valor total da compra com desconto: ", valortotal - (valortotal*0.02) )
    print("Você economizou: ", valortotal*0.02,"reais")
elif quantidade>2 and quantidade<=5:
    print("O valor total da compra com desconto: ", valortotal - (valortotal*0.05))
    print("Você economizou: ", valortotal*0.05,"reais")
elif quantidade>5 and quantidade<10:
    print("O valor total da compra com desconto: ", valortotal - (valortotal*0.1))
    print("Você economizou: ", valortotal*0.1,"reais")
elif quantidade>=10:
    print("O valor total da compra com desconto: ", valortotal - (valortotal*0.15))
    print("Você economizou: ", valortotal*0.15,"reais")