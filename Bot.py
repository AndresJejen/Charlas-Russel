Bot =   {
            "Hola": "Hola ¿Cómo estas hoy?",
            "Cuentame un chiste": "¿Qué hacian dos pollitos en frente de un asadero? --- viendo una pelicula de terror",
            "Cuentame otro": "¿Que hace un perro con un taladro? --- Taladrando",
            "Chao": "Adios, espero verte mañana"
        }

mensaje = ""

while (mensaje != "Chao"):
    mensaje = input(" Tu: ")
    print(Bot[mensaje])