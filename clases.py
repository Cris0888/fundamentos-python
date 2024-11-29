class Persona:
    nombre = 'christian'
    edad = 0
    ciudad = 'bogota'

# si queremos imprimir una clase como un diccionario llave valor primero debemos convertir la clase con el metodo __dict__.item() lo que hace este metodo es iterar sobre los atributos de la clase o de una instancia, 

for nombre,valor in Persona.__dict__.items():
    #lo que hace if not nombre.startswith('__'): es negar la condicion if not solamente se ejecuta  cuando de false se activa el if not este if lo que hace es eliminar los atributos del lenguaje (o los atributos magicos)
    if not nombre.startswith('__'):
        print(f"{nombre}: {valor}")

#clases con constructores con el metodo __init__ 

class Automovil:
    def __init__(self,tipo,marca,color):
        self.tipo=tipo
        self.marca=marca
        self.color=color
        
    
#instancia de la clase Automovil 
automovil=Automovil("automovil","toyota","blanco")

#si queremos ver un dato de una instancia ponemos el nombre de la instancia.(punto) nombre del dato queremos visualizar

print(automovil.color)#blanco

#si queremos recorrer todos los datos de la instancia ponemos nombre de la instancia.__dict__items()

for tipo , marca , in automovil.__dict__.items():
    print(f"{tipo} {marca}")