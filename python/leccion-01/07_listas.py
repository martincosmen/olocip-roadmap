# Crear una lista
jugadores = ["Lamine", "Pedri", "Gavi"]

# Acceder a un elemento
print(jugadores[0])

# Modificar un elemento
jugadores[0] = "Nico"

# Añadir un elemento al final
jugadores.append("Cubarsí")

#Añadir un elemento en una posición específica
jugadores.insert(1, "Bernal")

# Eliminar un elemento por su valor 
jugadores.remove("Gavi")

# Eliminar un elemento por su posición 
jugadores.pop(1)

#Contar elementos de una lista
len(jugadores)

# Añadimos a Rodri solamente si no está ya en la lista.

if "Rodri" not in jugadores:
    jugadores.append("Rodri")
    print("Rodri ha sido añadido")

else:
    print("Rodri ya estaba en la lista")
