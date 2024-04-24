N=int(input("Ingrese el primer numero: "))
Z=int(input("Ingrese el segundo numero: "))
K=int(input("Ingrese el tercer numero: "))

if N>Z and N>K:
    P= N%2
    if P==0:
        print("El numero mayor es",N,"y es PAR")
    else:
        print("El numero mayor es",N,"y es IMPAR")
else:
    if Z>N and Z>K:
        P= N%2
        if P==0:
            print("El numero mayor es",Z,"y es PAR")
        else:
            print("El numero mayor es",Z,"y es IMPAR")
    else:
        if K>N and K>Z:
            P= K%2
            if P==0:
                print("El numero mayor es",K,"y es PAR")
            else:
                print("El numero mayor es",K,"y es IMPAR")

        
