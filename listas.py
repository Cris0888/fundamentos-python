#las listan pueden almacenar cualquier tipo de dato se crean de dos maneras con [] 
lista1=["hola",1,True,False,55,"chistian",]
#tambien podemos crearla con la palabra list
lista2=list(("hi",2,5,True))

#si queremos ver la ultima pocion de la lista ponemos -1

print(lista1[-1])

#si queremos ver cuantos valores tiene la lista ponemos len
print(len(lista1))

#para aceder alas posiciones de las listas ponemos el nombre de la lista y la pocion del dato queremos ver de esa lista  por defecto inicia en 0

print(lista1[0]) # hola

#si queremos que la lista valla desde una posicion hasta cierta posicion que le espesifiquemos el primer numero es desde donde queremos que valla y el segundo numero hasta donde queremos que valla por defecto llega hasta una posicion antes de la espesificada
#-------------------------------------MODIFICAR EN LA LISTA--------------------------------------
#modificar datos hay varias formas una nos modifica desde la posicion que le indiquemos con insert la otra es reseteando la lista

#si queremos modificar un dato lo hacemos reseteando la lista primero ponemos la posicion y despues como se va llamar


#reseteando la lista
lista1[0] = "grajales"


#-----------------------AÑADIR EN LALISTA-----------------------

#para añadir tenemos varias formas una de ellas es añadiendo en la ultima posicion de la lista y la otra nos añade el elemento en la posicion que le especifiquemos 

# con append nos inserta el dato en la ultima pocion de la lista 
lista1.append("hello")

# de donde le especifiquemos
lista1.insert(1,"unooo")
print(lista1)
#-----------------------ELIMINAR EN LA LISTA--------------------------------------------

#hay varias formas de eliminar una de ellas es elimina el elemento de la ultima posicion de la lista la segunda es elimina el elemento que le especifiquemos como se llama en la lista  y la tercera forma es poniendo la posicion de el elemento y la ultima elimina todos los elementos de la lista pero sin borrar la lista

#elimina el ultimo valor de la lista
lista1.pop()

#elimina como este llamado en la lista
lista1.remove("grajales")

#elimina con la posicion en la que este en la lista el elemento 
del lista1[1]

#elimina todos los elementos de la lista 
lista1.clear()

#Métodos comunes de las listas

#index(valor): Devuelve el índice de la primera aparición de un valor.

print(lista1.index("hola"))  # 1

#count(valor): Cuenta cuántas veces aparece un valor.

numeros = [1, 2, 2, 3]
print(numeros.count(2))  # 2

#sort(): Ordena los elementos en orden ascendente.

lista1.sort()
print(numeros)  

#reverse(): Invierte el orden de los elementos.

lista1.reverse()

#copy(): Crea una copia superficial de la lista.

copia = lista1.copy()
