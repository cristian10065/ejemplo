
#metodo constructos que nos sirve para recibir los datos
class Persona:
    def __init__(self, nombre, apellido, edad, correo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.telefono = telefono
        
#definimos una funcions para establecer la estructura con que la almacenamos los documentos     
    def formato_doc(self):
        return {
            'nombre' : self.nombre,
            'apellido' : self.apellido,
            'edad' : self.edad,
            'correo' : self.correo,
            'telefono' : self.telefono
        }


