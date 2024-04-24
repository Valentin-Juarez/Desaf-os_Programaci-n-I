año=0
def bisiesto(Numero):
    if año<4:
        return False
        print("El año no es bisiesto")
    for i in range(4, año):
         if Numero % i == 0:
            return False
            print("El numero no es primo")
    return True
año=int(input("Ingrese un numero:"))
if bisiesto(año):
    print("El año",año,"es bisiesto")