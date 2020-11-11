def verificarInteiros():
    try:
        numeroInt = int(input("Insira um valor numerico inteiro, sem virgulas: "))
    except(ValueError):
        return False
    else:
        print("O valor está correto")

while verificarInteiros() == False:
    print("Valor invalido, favor inserir um numero inteiro.")


def verificarFloat():
    try:
        numeroFloat = float(input("Insira um valor numerico positivo: "))
    except:
        return False
    if numeroFloat < 0:
        return False
    else:
        print("O valor está correto")

while verificarFloat() == False:
    print("Valor invalido, favor inserir um numero positivo, acima de 0.")