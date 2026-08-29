# Chatbot de Ciberseguridad - Copias de Seguridad
# Actividad 5

def responder(pregunta):
    pregunta = pregunta.lower()

    if "hola" in pregunta or "buenas" in pregunta:
        return "Hola. Soy un chatbot de ciberseguridad especializado en copias de seguridad."

    elif "backup" in pregunta or "copia de seguridad" in pregunta:
        return ("Una copia de seguridad es una copia de los archivos importantes "
                "que permite recuperarlos si se pierden, dañan o eliminan.")

    elif "importante" in pregunta or "importancia" in pregunta:
        return ("Las copias de seguridad son importantes porque ayudan a proteger "
                "la información frente a pérdidas accidentales, daños o problemas "
                "con los dispositivos.")

    elif "cada cuanto" in pregunta or "frecuencia" in pregunta:
        return ("Las copias de seguridad deben realizarse periódicamente. "
                "La frecuencia depende de qué tan importante y qué tan seguido "
                "cambie la información.")

    elif "donde" in pregunta or "dónde" in pregunta:
        return ("Es recomendable conservar las copias de seguridad en un lugar "
                "diferente al dispositivo principal. También se pueden utilizar "
                "medios de almacenamiento externos o servicios de almacenamiento "
                "en la nube.")

    elif "proteger" in pregunta or "seguridad" in pregunta:
        return ("Para proteger una copia de seguridad se recomienda utilizar "
                "contraseñas seguras, controlar el acceso y mantener actualizado "
                "el sistema.")

    elif "perdi" in pregunta or "perdí" in pregunta or "recuperar" in pregunta:
        return ("Si pierdes información, primero debes comprobar si existe una "
                "copia de seguridad disponible. Después puedes utilizarla para "
                "recuperar los archivos necesarios.")

    elif "consejo" in pregunta or "recomendacion" in pregunta or "recomendación" in pregunta:
        return ("Mi recomendación es realizar copias de seguridad periódicamente, "
                "comprobar que funcionen correctamente y mantener al menos una "
                "copia separada del dispositivo principal.")

    elif "salir" in pregunta or "adios" in pregunta or "adiós" in pregunta:
        return "Hasta luego. Recuerda proteger y realizar copias de seguridad de tu información."

    else:
        return ("No tengo una respuesta para esa pregunta. "
                "Puedes preguntarme sobre backups, copias de seguridad, "
                "recuperación de archivos o protección de información.")


print("==============================================")
print("   CHATBOT DE CIBERSEGURIDAD - BACKUPS")
print("==============================================")
print("Escribe 'salir' para terminar.")
print()

while True:
    pregunta = input("Tú: ")

    respuesta = responder(pregunta)

    print("Chatbot:", respuesta)
    print()

    if "salir" in pregunta.lower() or "adios" in pregunta.lower() or "adiós" in pregunta.lower():
        break
Función responder()
def responder(pregunta):

Esta función recibe la pregunta escrita por el usuario y determina qué respuesta debe entregar el chatbot.

Conversión a minúsculas
pregunta = pregunta.lower()

Convierte el texto a minúsculas para que el programa pueda reconocer las palabras aunque el usuario las escriba con mayúsculas.

Condiciones if y elif

Por ejemplo:

elif "backup" in pregunta or "copia de seguridad" in pregunta:

El programa comprueba si la pregunta contiene alguna de esas palabras. Si la encuentra, devuelve una respuesta relacionada con las copias de seguridad.

return
return "Una copia de seguridad es..."

return permite devolver la respuesta que debe mostrar el chatbot.

input()
pregunta = input("Tú: ")

Permite que el usuario escriba una pregunta directamente en la consola.

while True
while True:

Hace que el chatbot continúe funcionando y permitiendo preguntas hasta que el usuario decida salir.

break
break

Finaliza el programa cuando el usuario escribe una palabra para salir.
