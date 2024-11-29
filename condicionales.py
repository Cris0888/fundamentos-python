#toma de deciciones if elif else ejemplo entrada si es mayor de edad

nombre=input("escriba su nombre: ")
edad=int(input("escriba su edad: "))
if edad>=55:
    print(f"{nombre} puede ingresar bajo su responsabilidad")

elif edad >=18:
    print(f"{nombre} puede ingresar")

else:
    print("no puede ingresar por ser menor de edad")
