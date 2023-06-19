import openai
import pyttsx3
import speech_recognition as sr
from googlesearch import search

# Configura tu clave de API
openai.api_key = 'TU_CLAVE_DE_API'

# Inicializa el motor de síntesis de voz
engine = pyttsx3.init()

def obtener_respuesta(pregunta):
    # Envía la pregunta a la API de ChatGPT
    respuesta = openai.Completion.create(
        engine='text-davinci-003',
        prompt=pregunta,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=15
    )

    # Extrae y devuelve la respuesta generada por ChatGPT
    return respuesta.choices[0].text.strip()

# Inicializa el reconocimiento de voz
r = sr.Recognizer()

# Bucle principal del asistente virtual
while True:
    # Escucha la entrada de voz del usuario
    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)

    try:
        # Utiliza el reconocimiento de voz para convertir el audio en texto
        entrada = r.recognize_google(audio, language="es")

        # Finaliza el bucle si el usuario dice "salir"
        if entrada.lower() == "salir":
            break

        print("Usuario: " + entrada)

        if "buscar en Google" in entrada:
            # Realiza una búsqueda en Google
            busqueda = entrada.replace("buscar en Google", "").strip()
            resultados = search(busqueda, num_results=1)

            # Obtiene el primer resultado de búsqueda
            primer_resultado = next(resultados, None)

            if primer_resultado:
                respuesta = "Aquí tienes el resultado de búsqueda en Google: " + primer_resultado
            else:
                respuesta = "No se encontraron resultados en Google para esa búsqueda."

        else:
    
            respuesta = obtener_respuesta(entrada)

        # Imprime la respuesta en la consola
        print("Asistente: " + respuesta)

        # Utiliza el motor de síntesis de voz para reproducir la respuesta
        engine.say(respuesta)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError as e:
        print("Error al solicitar los resultados del reconocimiento de voz; {0}".format(e))
