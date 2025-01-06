idade = 0
while idade <=0:
    idade = int(input("Informe a idade: "))
    if idade >=0:
        print("Ok")
    else: 
        print("idade insulficiente")
        while idade <0:
            idade = int(input("Informe uma idade sufuciente: "))

print ("Idade informada: ", idade)