#los dicionarios utilizan un formato llamado llave valor en donde llamas la llave y te imprime el valor ejemplo las especificaciones tecnicas de un cumputador

mac={
    "nombre": "mac",
    "ram": 4,
    "sistema operativo":"ios",
    "precio": 2000.000,
    "marca": "iphone"

}
#para mostrar el valor de un diccionario debemos llamar la llave

print(mac["ram"])#4

#para imprimir el dicionario completo usamos un for para iterarlo y despues le damos el parametro .items()



for llave, valor in mac.items():
    print(f"{llave}: {valor}")

#-------------------------------------ACTUALIZAR DICCIONARIO------------------------------------------

mac["nombre"]="macBook"

#-------------------------------------AÑADIR AL DICCIONARIO------------------------------------
#si el diccionario ve que la llave no existe lo agrega en la ultima pocicion del diccionario

mac["ciudad"] = "california"

#---------------------------------------ELIMINAR DATOS DEL DICCIONARIO------------------------------------------
#existen varias formas de eliminar datos de un diccionario una de ellas elimina el ultimo valor del diccionario la otra forma elimina el dato en la pocicion que le indiquemos

#elimina el ultimo valor del diccionario 

mac.popitem()

#elimina el valor en la posicion que le especifiquemos

del mac["ciudad"]


# Recorrer las llaves
for llave in mac:
    print(llave)

# Recorrer los valores
for valor in mac.values():
    print(valor)

# Recorrer llaves y valores
for llave, valor in mac.items():
    print(f"{llave}: {valor}")

#------------------------------METODOS UTILES-----------------------------------------

# Obtener todas las llaves
llaves = mac.keys()

# Obtener todos los valores
valores = mac.values()

# Obtener  llave-valor
llave_valor = mac.items()

# Limpiar el diccionario
mac.clear()

# Verificar si una clave existe
if "nombre" in mac:
    print("¡La clave 'nombre' existe!")

