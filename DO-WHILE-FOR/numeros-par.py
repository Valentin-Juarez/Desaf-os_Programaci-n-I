numero_par=0
numero_impar=0
suma_par=0
for i in range(4):
    numero=int(input("Ingrese un numero:"))
    if numero%2==0:
        suma_par=suma_par+numero
        numero_par+=1
        print(numero_par)
    else:
        numero_impar=+1
print("La cantidad de numeros impares es",numero_impar)
print("La cantidad de numeros pares es",numero_par,"y sumados da",suma_par)
