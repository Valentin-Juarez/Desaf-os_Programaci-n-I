R= int(input("Que desea hacer:"
         "1-Cambiar pesos a dolares" 
         "2-Cambiar dolares a pesos: "))
print(R)
if R==1:
    N=int(input("Ingrese un monto en pesos: "))
    T=N/900
    print("La cantidad de dolares es:",T,)
else:
    if R==2:
        Z=int(input("Ingrese otro monto en dolar: "))
        V=Z*900
        print("La cantidad de pesos es:",V,)
    else:
        print("Por favor marcar SOLO el numero 1 o 2")

