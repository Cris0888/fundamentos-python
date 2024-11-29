#las funciones siempre reciben parametros ya sea por medio del usuario o con datos que ya estan en variables
def suma(numero1,numero2):
    return numero1+numero2

print(suma(10,66))
#funcion suma que recibe parametros por medio del usuario
def sumar():
    entrada1=int(input("introduce el primer numero: "))
    entrada2=int(input("introduce el segundo numero: "))
    return entrada1 + entrada2

resultado = sumar()

print(f"la suma es {resultado}")



