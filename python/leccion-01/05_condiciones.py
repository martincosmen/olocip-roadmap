valoracion = int(input("Introduce la valoración del jugador: "))

if valoracion >= 90:
    print("Jugador élite")

elif valoracion >= 70:
    print("Buen jugador")

elif valoracion >= 50:
    print("Jugador promedio")

else:
    print("Necesita mejorar")