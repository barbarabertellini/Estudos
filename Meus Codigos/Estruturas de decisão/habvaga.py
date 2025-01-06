idade = int(input("Digite da idade do candidato: "))

print(" 1 - Ensio Fundamental \n 2 - Ensino Médio \n 3 - Ensino Superior \n")
ensino = int(input("Digite o número de acordo com a escolaridade: "))

if (ensino==3) or (idade>=60 and ensino==2):
    print("Habilitado")
else:
    print("Não habilitado")