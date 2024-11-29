#si queremos usar arrays homogéneos y eficientes se debe usar el módulo array. los arrays solo soportan un solo tipo de dato si queremos usar que soporte todos los tipos para eso estan las listas 
from array import array
#si queremos crear un array lo hacemos de esta forma el i significa i de int este array solo soporta numeros enteros

""" Código	de los tipos numericos en python al usar arrays
'b'	signed char	entero (8 bits)
'B'	unsigned char	entero positivo (8 bits)
'i'	int	entero (32 bits)
'f'	float	flotante (32 bits)
'd'	double	flotante (64 bits) """
primer_array=(array("i",[1,2,3,4,5,6,7]))
# si queremos llamarlo lo hacemos de esta manera nombre del array y posicion del array
#--------------------------------ACTUALIZAR EL ARRAY--------------------------------
primer_array[0]=10

#-------------------------------AGREGAR AL ARRAY------------------------------------
#para agregar elementos a un array hay varias maneras una de ellas es añadiendo el valor al final del array y la otra forma es añadiendo el valor en la posicion que le indiquemos

#al final del array
primer_array.append(8)
#posicion que le indiquemos el primer numero es para indicar que posicion insertaremos ese dato y el segundo es el valor que le vamos asignar
primer_array.insert(2,100)
print(primer_array)

#---------------------------------------ELIMINAR EN EL ARRAY---------------------------------------------
#para eliminar elementos a un array hay varias maneras una de ellas es eliminando el valor por el indice del array y la otra forma es eliminandolo como este llamado en el array
#por indice del array aqui eliminamos el que este en la posicion 2
primer_array.pop(3)
#de esta forma se elimina como este llamado en el array
primer_array.remove(100)
print(primer_array)


