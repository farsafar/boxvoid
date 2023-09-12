import openai
import pyttsx3
import speech_recognition as sr
from googlesearch import search
from gtts import gTTS
import os

inicio = gTTS("Hola soy boxvoid, en que te puedo ayudar", lang="es")
inicio.save("inicio.mp3")
os.system("mpg123 inicio.mp3")

openai.api_key = 'tu api key '


engine = pyttsx3.init()

def obtener_respuesta(pregunta):
    respuesta = openai.Completion.create(
        engine='text-davinci-003',
        prompt=pregunta,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=15
    )


    return respuesta.choices[0].text.strip()


r = sr.Recognizer()


while True:
    
    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)

    try:
        
        entrada = r.recognize_google(audio, language="es")

        
        if entrada.lower() == "salir":
            break

        print("Usuario: " + entrada)

        if "buscar en Google" in entrada:
            
            busqueda = entrada.replace("buscar en Google", "").strip()
            resultados = search(busqueda, num_results=1)

           
            primer_resultado = next(resultados, None)

            if primer_resultado:
                respuesta = "Aquí tienes el resultado de búsqueda en Google: " + primer_resultado
            else:
                respuesta = "No se encontraron resultados en Google para esa búsqueda."

        else:
    
            respuesta = obtener_respuesta(entrada)

       
        print("Asistente: " + respuesta)

        
        RespuestaTTS = gTTS(respuesta, lang="es")
        RespuestaTTS.save("respuesta.mp3")
        os.system("mpg123 respuesta.mp3")
        os.system("rm -r respuesta.mp3")

    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError as e:
        print("Error al solicitar los resultados del reconocimiento de voz; {0}".format(e))
