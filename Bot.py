from MibancoFuncion import consultarValorApagar

Bot =   {
            "Hola": "Hola ¿Cómo estas hoy?",
            "Cuentame un chiste": "¿Qué hacian dos pollitos en frente de un asadero? --- viendo una pelicula de terror",
            "Cuentame otro": "¿Que hace un perro con un taladro? --- Taladrando",
            "Chao": "Adios, espero verte mañana",
            "consultar deuda": "Ok Ingresa los valores",
        }

mensaje = ""

while (mensaje != "Chao"):
    try:
        mensaje = input(" Tu: ")
        print(Bot[mensaje])

        if (mensaje == "consultar deuda"):
            consultarValorApagar()

    except:
        print("No entiendo tu pregunta -- repitemela por favor")