Numero=int(input("Ingrese un numero:"))
Centena=int(Numero/100) 
Decena= int((Numero%100)/10)
Unidad= Numero%10
print(str(Unidad)+str(Decena)+str(Centena))