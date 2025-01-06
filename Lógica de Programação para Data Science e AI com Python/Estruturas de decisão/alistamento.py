nascimento = int(input("Digite o ano de nascimento: "))
from datetime import date
year_ = date.today().year

if ((date.today().year) - nascimento) >=18:
    print("Deve se alistar")
else:
    print("Não deve se alistar")