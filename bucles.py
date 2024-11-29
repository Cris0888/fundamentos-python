#bucles hay 2 los ciclos cuando le especificamos el fin y los otros que son infinitos hasta que se cumpla dicha condicion 

#ciclo for va desde donde le especifiquemos y cuando se deja de cumplir la condicion deja de iterar el ciclo no solo es con numeros tambien recorre cadenas de texto

#numeros ira desde 0 hasta 20 que es el resultado de la variable numero 
#--------------------------------------for---------------------------------------------------------------------
numero=20

for i in range(0,numero):
    print(f"hola soy el numero {i}")

#cadenas de texto 
Nombre="christian"
for nombre in Nombre:
    print(nombre)

# tambien si queremos iterar un dicionario o lista o cualquier elemento podremos hacerlo

#iterar con un diccionario tenemos que usar items() para poder iterar el elemento
diccionario={
    "nombre":"christian",
    "apellido":"grajales",
    "ciudad":"bogota"
}
for llave,valor in diccionario.items():
    print(f"{llave}: {valor}")

#iterar con listas si queremos que nos enumere la iteracion debemos poner enumerate() y el nombre de la lista

nombres=["christian","camilo","restrepo","grajales"]

for i in nombre:
    print(i)

#no solo esta range y iterar cadenas de texto

#Aquí tienes una lista de métodos y funciones que puedes usar con un for:

#enumerate(): Índice y elemento.
#zip(): Iterar en paralelo.
#reversed(): Iterar en orden inverso.
#sorted(): Iterar en orden.

#-----------------------------------while-----------------------------------------------------------------------
#este ciclo se cumple mientras la variable ciclo es menor que 10 el ciclo llegara hasta una iteracion antes el cual sera 9
ciclo=0
while ciclo<10:
    print(f"hola soy el ciclo #{ciclo}")
    ciclo+=1
    continue

#ciclos con la entrada de datos por medio del usuario

entrada1 = 0
entrada2 = int(input("ingrese hasta donde quiere que termine le ciclo: "))

while entrada1<entrada2:
    print(f"soy el numero {entrada1}")
    if entrada1>entrada2:
        break
    entrada1+=1
    

