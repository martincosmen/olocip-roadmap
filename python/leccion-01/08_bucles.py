# ==========================================
# BUCLES EN PYTHON
# ==========================================


# ==========================================
# 1. BUCLE FOR
# ==========================================

# Se utiliza para recorrer elementos de una lista,
# o para repetir una acción un número determinado de veces.

jugadores = ["Lamine", "Pedri", "Gavi", "Cubarsí"]

for jugador in jugadores:
    print(jugador)

# Resultado:
# Lamine
# Pedri
# Gavi
# Cubarsí


# ==========================================
# 2. FOR + IF
# ==========================================

# Podemos utilizar condiciones dentro de un bucle.

numeros = [5, 12, 8, 25, 3, 18]

for numero in numeros:
    if numero >= 10:
        print(numero)

# Solo se imprimen los números mayores o iguales que 10.


# ==========================================
# 3. RANGE()
# ==========================================

# range() genera una secuencia de números.

for numero in range(5):
    print(numero)

# Resultado:
# 0
# 1
# 2
# 3
# 4

# IMPORTANTE:
# range(5) empieza en 0 y llega hasta ANTES de 5.


# ==========================================
# 4. RANGE(INICIO, FIN)
# ==========================================

# Podemos indicar desde qué número empezar.

for jornada in range(1, 6):
    print("Jornada", jornada)

# Resultado:
# Jornada 1
# Jornada 2
# Jornada 3
# Jornada 4
# Jornada 5

# IMPORTANTE:
# El inicio se incluye.
# El final NO se incluye.


# ==========================================
# 5. RANGE(INICIO, FIN, PASO)
# ==========================================

# El tercer parámetro indica cuánto avanzamos
# en cada vuelta.

for numero in range(1, 11, 2):
    print(numero)

# Resultado:
# 1
# 3
# 5
# 7
# 9

# range(1, 11, 2)
# 1 = inicio
# 11 = fin (no incluido)
# 2 = paso


# ==========================================
# 6. RECORRER UNA LISTA CON SU POSICIÓN
# ==========================================

jugadores = ["Lamine", "Pedri", "Gavi", "Cubarsí"]

for posicion in range(4):
    print(posicion, jugadores[posicion])

# Resultado:
# 0 Lamine
# 1 Pedri
# 2 Gavi
# 3 Cubarsí

# Las listas empiezan en la posición 0.


# ==========================================
# 7. LISTAS DENTRO DE LISTAS
# ==========================================

# Podemos guardar varios datos de cada jugador.

jugadores = [
    ["Lamine", 18, "Delantero"],
    ["Pedri", 23, "Centrocampista"],
    ["Gavi", 21, "Centrocampista"]
]

# Podemos acceder a los datos mediante índices:

jugador = jugadores[0]

print(jugador[0])  # Nombre
print(jugador[1])  # Edad
print(jugador[2])  # Posición


# También podemos recorrer todos los jugadores:

for jugador in jugadores:
    print(jugador[0])

# Resultado:
# Lamine
# Pedri
# Gavi


# ==========================================
# 8. FOR + LISTAS + CONDICIONES
# ==========================================

# Podemos filtrar jugadores según sus datos.

for jugador in jugadores:
    if jugador[1] < 22:
        print(jugador[0], "-", jugador[1], "años")

# Solo muestra jugadores menores de 22 años.


# ==========================================
# 9. BUCLE WHILE
# ==========================================

# while repite el código MIENTRAS una condición
# sea verdadera.

jornada = 1

while jornada <= 5:
    print("Jornada", jornada)
    jornada = jornada + 1

# Resultado:
# Jornada 1
# Jornada 2
# Jornada 3
# Jornada 4
# Jornada 5

# Es MUY IMPORTANTE modificar la variable.
# Si no cambia, podemos crear un bucle infinito.


# ==========================================
# 10. WHILE CON DECREMENTO
# ==========================================

# La variable también puede disminuir.

contador = 5

while contador > 0:
    print(contador)
    contador = contador - 1

# Resultado:
# 5
# 4
# 3
# 2
# 1


# ==========================================
# 11. WHILE + IF / ELSE
# ==========================================

jornada = 1

while jornada <= 5:

    if jornada == 3:
        print("Partido importante")
    else:
        print("Jornada", jornada)

    jornada = jornada + 1

# Resultado:
# Jornada 1
# Jornada 2
# Partido importante
# Jornada 4
# Jornada 5


# ==========================================
# 12. BREAK
# ==========================================

# break termina COMPLETAMENTE el bucle.

jornada = 1

while jornada <= 10:

    print("Jornada", jornada)

    if jornada == 5:
        break

    jornada = jornada + 1

# Resultado:
# Jornada 1
# Jornada 2
# Jornada 3
# Jornada 4
# Jornada 5

# Cuando jornada llega a 5, break termina el bucle.


# ==========================================
# 13. CONTINUE
# ==========================================

# continue salta la vuelta actual y continúa
# con la siguiente.

for jornada in range(1, 6):

    if jornada == 3:
        continue

    print("Jornada", jornada)

# Resultado:
# Jornada 1
# Jornada 2
# Jornada 4
# Jornada 5

# La jornada 3 se salta, pero el bucle continúa.


# ==========================================
# 14. BREAK VS CONTINUE
# ==========================================

# break:
# 🛑 Termina completamente el bucle.

# continue:
# ⏭️ Salta la vuelta actual y continúa.


# ==========================================
# 15. LEN() DENTRO DE UN BUCLE
# ==========================================

# len() devuelve la cantidad de elementos
# o caracteres.

jugadores = ["Lamine", "Pedri", "Gavi", "Cubarsí", "Rodri"]

for jugador in jugadores:
    if len(jugador) > 4:
        print(jugador)

# Resultado:
# Lamine
# Pedri
# Cubarsí
# Rodri


# ==========================================
# 16. CONTADOR
# ==========================================

# Podemos utilizar una variable para contar
# cuántos elementos cumplen una condición.

edades = [17, 23, 20, 18, 30]

contador = 0

for edad in edades:

    if edad < 21:
        contador = contador + 1

print("Jugadores jóvenes:", contador)

# Resultado:
# Jugadores jóvenes: 3


# IMPORTANTE:
# contador = contador + 1
# NO suma el valor del elemento.
# Simplemente aumenta el contador en 1.


# ==========================================
# 17. ACUMULADOR / SUMA
# ==========================================

# Podemos utilizar una variable para acumular
# valores.

edades = [18, 23, 21, 18]

suma = 0

for edad in edades:
    suma = suma + edad

print("Suma:", suma)

# Resultado:
# Suma: 80


# DIFERENCIA:
#
# contador = contador + 1
# → cuenta elementos
#
# suma = suma + edad
# → suma valores


# ==========================================
# 18. CALCULAR UNA MEDIA
# ==========================================

edades = [18, 23, 21, 18]

suma = 0

for edad in edades:
    suma = suma + edad

media = suma / len(edades)

print("Media:", media)

# Resultado:
# Media: 20.0


# ==========================================
# 19. EJEMPLO COMPLETO
# ==========================================

# Podemos combinar varios conceptos.

jugadores = [
    ["Lamine", 18],
    ["Pedri", 23],
    ["Gavi", 21],
    ["Cubarsí", 18]
]

contador = 0
suma_edades = 0

for jugador in jugadores:

    if jugador[1] < 22:
        contador = contador + 1
        suma_edades = suma_edades + jugador[1]

print("Jugadores jóvenes:", contador)
print("Suma de edades:", suma_edades)

# Resultado:
# Jugadores jóvenes: 3
# Suma de edades: 57


# ==========================================
# RESUMEN
# ==========================================

# FOR
# → Recorre elementos o repite una acción.

# WHILE
# → Repite mientras una condición sea verdadera.

# RANGE()
# → Genera una secuencia de números.

# IF
# → Comprueba una condición dentro del bucle.

# BREAK
# → Termina completamente el bucle.

# CONTINUE
# → Salta la vuelta actual y continúa.

# LEN()
# → Cuenta elementos o caracteres.

# CONTADOR
# → Cuenta cuántos elementos cumplen una condición.

# ACUMULADOR
# → Suma o acumula valores.

