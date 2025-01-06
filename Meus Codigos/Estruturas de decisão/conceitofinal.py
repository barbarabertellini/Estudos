nota = float(input("Digite a nota: "))

if nota>90:
    print("A")
elif nota>=75 and nota<=90:
    print("B")
elif nota>=60 and nota<75:
    print("C")
elif nota>=40 and nota<60:
    print("D")
elif nota>=20 and nota<40:
    print("E")
elif nota<20:
    print("F")