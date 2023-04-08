
from flask import Flask, render_template, request, redirect, url_for
from config import *
from persona import Persona
from bson import ObjectId
from pymongo import MongoClient

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/"
con_bd = Conexion()
app = Flask(__name__)

#------------------------------------------------------------------------------------
@app.route('/')
def index():
    personas = con_bd['Personas'] #para hacer la consulta de datos
    PersonasRegistradas = personas.find()
    return render_template('index.html', personas = PersonasRegistradas)
    
#-----------------------------------------------------------------------------
@app.route('/todos')
def todos():
    personas=con_bd['Personas']
    PersonasRegistradas=personas.find()
    return render_template('index.html', res=PersonasRegistradas)

#Buscará los datos donde el atributo "nombre" inicie por la letra c
@app.route('/nombresc')
def nombresc():
    personas=con_bd['Personas']
    PersonasRegistradas=personas.find({'nombre':{'$regex':'^c'}})
    return render_template('index.html', res=PersonasRegistradas)

#Búsqueda con ordenamiento
#Buscará todos los campos en la colección y los ordenará en orden descendente según el campo, en este caso "edad".
@app.route('/edad')
def edad():
    personas=con_bd['Personas']
    PersonasRegistradas = personas.find().sort("edad", -1)
    return render_template('index.html', res=PersonasRegistradas)

#Buscara el espacio donde el nombre sea meramente alan
@app.route('/nombre')
def nombre():
    personas=con_bd['Personas']
    PersonasRegistradas = personas.find({"nombre": "alan"})
    return render_template('index.html', res=PersonasRegistradas)

#buscara le edad entre un rango mayor a 18 y menor a 22
@app.route('/rango')
def rango():
    personas=con_bd['Personas']
    PersonasRegistradas = personas.find({'edad': { '$gt': '18', '$lt': '22' }})
    return render_template('index.html', res=PersonasRegistradas)

#buscara todos aquellos nombres que inien o tengas las letras "cr" no importa en que parte de la palabras dentro del nombre se encuentre
@app.route('/nombrevariables')
def nombrevariables():
    personas=con_bd['Personas']
    PersonasRegistradas = personas.find({"nombre": {"$regex": "^cr"}})
    return render_template('index.html', res=PersonasRegistradas)

#-------------------------------------------------------------------------------


@app.route('/guardar_persona', methods=['POST'])
def agregarPersona():
    personas = con_bd['Personas']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']
    correo = request.form['correo']
    telefono = request.form['telefono']
    
    if nombre and apellido and edad and correo and telefono:
        persona = Persona(nombre, apellido, edad, correo, telefono)
        personas.insert_one(persona.formato_doc())
        return redirect(url_for('index'))
    else:
        return "Hay Algo Mal"

#----------------------------------------------------------------------------------
@app.route('/eliminar_persona/<string:id_persona>')
def eliminar(id_persona):
    personas = con_bd['Personas'] #si no existe la conexion a la base de datos entonces se crea, de lo contrario consulta la informacion
    personas.delete_one({'_id':ObjectId(id_persona)}) #recibe un parametro que sirve para buscar y eliminar ese parametro en la base de datos
    return redirect(url_for('index')) #estamos redirigiendo a una funcion, en caso de cumplir la anterior funcion

#----------------------------------------------------------------------------------------

@app.route('/editar_persona/<string:id_persona>', methods=['POST'])
def editar(id_persona):
    personas = con_bd['Personas']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']
    correo = request.form['correo']
    telefono = request.form['telefono']
    
    if nombre and apellido and edad and correo and telefono:
        personas.update_one({'id':id_persona}, {'$set':{'nombre':nombre, 'apellido':apellido, 'edad':edad, 'correo':correo, 'telefono':telefono}})
        return redirect(url_for('index'))
    else:
        return "Hay Algo Mal - Error"

#------------------------------------------------------------------------------------------------
if __name__ =='__main__':
    app.run(debug=True)
    
