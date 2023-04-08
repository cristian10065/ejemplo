

from pymongo import MongoClient
import certifi

MONGO = 'mongodb+srv://cristianelianhernandez:Cristian1006532866@cluster0.gkdkseq.mongodb.net/?retryWrites=true&w=majority'

certificado = certifi.where()

def Conexion():
    try:
        Client = MongoClient(MONGO, tlsCAFile=certificado)
        db = Client["db_personas"]
    except ConnectionError:
        print('Error De Conexion')
    return db

