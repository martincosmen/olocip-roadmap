
# AND
# ==========================================
# "and" significa "Y".
# Para que el resultado sea True, todas las
# condiciones deben ser True.

# True and True   -> True
# True and False  -> False
# False and True  -> False
# False and False -> False


# Ejemplo:

edad = 25
tiene_entrada = True

if edad >= 18 and tiene_entrada:
    print("Puedes acceder")
else:
    print("No puedes acceder")


# ==========================================
# OR
# ==========================================

# "or" significa "O".
# Para que el resultado sea True, al menos una
# de las condiciones debe ser True.

# True or True    -> True
# True or False   -> True
# False or True   -> True
# False or False  -> False


# Ejemplo:

es_socio = False
tiene_invitacion = True

if es_socio or tiene_invitacion:
    print("Puedes acceder")
else:
    print("No puedes acceder")


# ==========================================
# NOT
# ==========================================

# "not" sirve para negar o invertir un valor booleano.

# not True  -> False
# not False -> True


# Ejemplo:

esta_lesionado = False

if not esta_lesionado:
    print("El jugador puede jugar")
else:
    print("El jugador no puede jugar")


# ==========================================
# LAS COMPARACIONES DEVUELVEN BOOLEANOS
# ==========================================

# Una comparación utilizando ==, >, <, >=, <= o !=
# devuelve automáticamente True o False.

respuesta = "si"

resultado = respuesta == "si"

print(resultado)

# En este caso:
# "si" == "si"
# El resultado es True.


# ==========================================
# EJERCICIO PRÁCTICO
# ==========================================

# Preguntamos si el jugador está lesionado.

respuesta_lesionado = input("¿Está el jugador lesionado? (si/no) ")

# La comparación devuelve directamente True o False.

lesionado = respuesta_lesionado == "si"


# Preguntamos si el jugador está convocado.

respuesta_convocado = input("¿Está el jugador convocado? (si/no) ")

# La comparación devuelve directamente True o False.

convocado = respuesta_convocado == "si"


# El jugador puede jugar solamente si:
# Está convocado Y NO está lesionado.

if convocado and not lesionado:
    print("El jugador está disponible para el partido")
else:
    print("El jugador tendrá que descansar el fin de semana")