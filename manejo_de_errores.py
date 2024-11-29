#el manejo de errores se usa cuando creamos una funcion o cualquier tipo de codigo y cuando lo vamos a correr y no estamos preparados para errores como pueden ser del usuario o del mismo programa al usar el manejo de errores si el programa nota un error sigue corriendo linea por linea solo nos dice que tipo de error sucedio pero si no usamos manejo de errores el programa se para y se cae el sistema lo que con el manejo de errores nos dice que tipo de error sucedio ay muchos tipos errores con los que podemos usar como los son

#SyntaxError	Hay un error de sintaxis en el código.
#ZeroDivisionError	Divides un número por cero.
#TypeError	Realizas una operación con tipos incompatibles.
#ValueError	El tipo es correcto, pero el valor no es apropiado.
#IndexError	Accedes a un índice fuera del rango de una secuencia.
#KeyError	Accedes a una clave que no existe en un diccionario.
#AttributeError	Usas un atributo que no existe en un objeto.
#FileNotFoundError	Intentas abrir un archivo que no existe.
#NameError	Usas una variable que no ha sido definida.
#OverflowError	El resultado de una operación excede el límite permitido.



try:
    numero1=int(input("ingresa el primero numero: "))
    numero2=int(input("ingresa el segundo numero: "))
    resultado=numero1/numero2

except ZeroDivisionError:
    print("no se puede dividir por zero intente un numero valido")

except ValueError:
    print("ingrese un valor correcto solo se permiten numeros enteros")

except Exception as error:
    print(f"error inesperado de typo {error}")

else:
    print(f"el resultado es {resultado}")

finally:
    print("gracias por probar el programa christian")





