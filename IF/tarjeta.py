N=int(input("Ingrese el monto:"))
C=int(input("Ingrese la forma de pago 1-Contado 2-Tarjeta 3-Debito: "))
if C==1:
    Z= N*0.10
    H=N-Z
    print("El monto ingresado es",N,"con un descuento de",Z,"con un importe total de ",H,)
else: 
    if C==2:
        Z= N*0.10
        H=N+Z
        print("El monto ingresado es",N,"con un Interes de",Z,"con un importe total de ",H,)
    else:
        if C==3:
            Z= N*0.05
            H=N+Z
            print("El monto ingresado es",N,"con un descuento de",Z,"con un importe total de ",H,)
        else:
            print("Ingrese los numeros 1,2 o 3 unicamente")

