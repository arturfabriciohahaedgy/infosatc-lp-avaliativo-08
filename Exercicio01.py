numero1 = []
def verificarInteiros(numero1):
    a = input("Insira um valor numerico inteiro: ")
    numero1.append(a)
    for x in numero1:
        if "." in x:
            numero1.clear()
            return False
        elif "" or " " in x:
            numero1.clear()
            numero1.insert(0, "0")
            return True
        else:
            return True      
while verificarInteiros(numero1) == False:
    print("Valor invalido, favor inserir um numero inteiro.")
    

