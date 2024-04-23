"""Supongamos que tenemos una base de datos de personas, por ejemplo:
database = {
            1:{
                "nombre1":"Pablo",
                "nombre2":"Diego",
                "apellido1":"Ruiz",
                "apellido2":"Picasso"
            },
            2:{
                "nombre1":"Elio",
                "apellido1":"Anci"
            },
            3:{
                "nombre1":"Elias",
                "nombre2":"Marcos",
                "nombre3":"Luciano",
                "apellido1":"Marcelo",
                "apellido2":"Gonzalez"
            }
}
Construir una funcion que permita recibir los nombres y apellidos de una persona, para verificar si se encuentra en la base de datos. La
función debería retornar el "id" o la key del diccionario que contiene a una persona con todos los nombres y apellidos pasados como
parametros a la funcion buscar_datos()
Ejemplo:
Si busco una persona cuyo nombre sea "Pablo Diego Ruiz Picasso", entonces, la llamada a la función será:
buscar_datos("Pablo", "Diego","Ruiz","Picasso", **database)
Donde cada uno de los primeros argumetos serán los nombres y apellidos (no necesariamente ordenados) y el último parametro, indicado con
asteriscos, sería la base de datos.
En base a esta llamada a la función, se debería retornar el valor de la key del diccionario que contiene los valores "Pablo, Diego, Ruiz,
Picasso"
buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database) -> 1
Donde 1 es la key que identifica al diccionario correspondiente que contiene todos esos valores (ni mas ni menos)"""


def buscar_datos(*args, database):
    for key, persona in database.items():
        # Convertimos los valores del diccionario a una lista
        valores = list(persona.values())
        # Comparamos si todos los argumentos están en la lista de valores
        if all(arg in valores for arg in args):
            return key
    
    # Si no se encuentra ninguna persona con todos los argumentos, retornamos None
    return None


database = {
    1: {
        "nombre1": "Pablo",
        "nombre2": "Diego",
        "apellido1": "Ruiz",
        "apellido2": "Picasso"
    },
    2: {
        "nombre1": "Elio",
        "apellido1": "Anci"
    },
    3: {
        "nombre1": "Elias",
        "nombre2": "Marcos",
        "nombre3": "Luciano",
        "apellido1": "Marcelo",
        "apellido2": "Gonzalez"
    }
}

resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", database=database)
print("el id de la persona es: ", resultado)  # Debería imprimir: 1

