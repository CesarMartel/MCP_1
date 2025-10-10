from pymongo import MongoClient
from django.conf import settings

client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB]
conversaciones = db["conversaciones"]

def guardar_mensaje(usuario, mensaje, respuesta):
    """Guarda un mensaje en la conversación del usuario."""
    conv = conversaciones.find_one({"usuario": usuario})
    nuevo = {"usuario": mensaje, "bot": respuesta}

    if conv:
        conversaciones.update_one({"usuario": usuario}, {"$push": {"mensajes": nuevo}})
    else:
        conversaciones.insert_one({
            "usuario": usuario,
            "mensajes": [nuevo]
        })

def obtener_conversacion(usuario):
    conv = conversaciones.find_one({"usuario": usuario})
    return conv["mensajes"] if conv else []
