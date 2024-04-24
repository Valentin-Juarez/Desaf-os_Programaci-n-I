def primo(Numero):
    if Numero<2:
        return False
        print("El numero no es primo")
    for i in range(2, Numero):
         if Numero % i == 0:
            return False
            print("El numero no es primo")
    return True

Numero=int(input("Ingrese un numero:"))
if primo(Numero):
    print("El numero",Numero,"es primo")
        