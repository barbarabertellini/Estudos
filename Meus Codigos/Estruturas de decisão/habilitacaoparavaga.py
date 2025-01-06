idade = int(input("Idade do candidato: "))
atividade = int(input("Tempo de atividade profissional: "))

if (idade<70) or (atividade>=25) or (idade>=70 and atividade>=30):
    print("Habilitado!")
else:
    print("Não habilitado")