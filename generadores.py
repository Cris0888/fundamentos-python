#los generadores permiten extraer valores de una funcion y despues almacenarlos
#(de uno en uno) en objebtos iterables (que se pueden correr)
#sin necesidad de almacenarlos todos ala vez en la memoria ram

#lo que hace esta funcion es iterar por medio de un ciclo for los multiplos del 7 el yield almacena todos los datos y cuando ya estan todos alamcenados se  los pasa al ciclo for y el ciclo for los itera en la varibale (i) despues se imprimen en pantalla ay varias maneras de mostrar los datos de los generadores tambien por medio de listas tuplas arreglos 

#usando for para mostrar los datos
def generadormultiplos7(limite):
    numero=1
    while numero<=limite:
        yield numero*7
        numero=numero+1

generador=generadormultiplos7(10)
for i in generador:
    print(i)


#usando listas para mostrar los datos
def generadormultiplos5(limite):
    numero=1
    while numero<=limite:
        yield numero*5
        numero=numero+1

generador=generadormultiplos5(10)
print(list(generador))

#usando tuplas para mostrar los datos 

def generadormultiplos6(limite):
    numero=1
    while numero<=limite:
        yield numero*5
        numero=numero+1

generador=generadormultiplos6(10)
print(tuple(generador))


#usando la funcion join para concatenar los valores y mostrarlos 

lista=["hola","mundo","andamos","programando","en","el","lenguaje","de","programacion","python"]

def generador_lista():
    for i in lista:
        yield i
list=generador_lista()
print(" ".join(list))

