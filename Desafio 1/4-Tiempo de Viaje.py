Tramo=0
while Tramo==0:
    Distancia=int(input("Duracion del tramo:"))
    if Distancia==0:
        Tramo=+1
        Hora=int(Tiempo/1)
        Minutos=int((Tiempo%int(Tiempo))*100) 
        valor= Minutos/60
        print("El viaje duro:",str(Hora),":",str(Minutos))
    else:
            Tiempo=Distancia*1.6