import openai
import pyttsx3
import speech_recognition as sr
from googlesearch import search
import wikipedia
import pywhatkit
from time import *

openai.api_key = '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'

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
        engine.say(entrada)

        if "Busca" in entrada:
             
             wikipedia.set_lang('es')
             busqueda = entrada.replace('Busca', '')
             respuestas = wikipedia.summary(busqueda , sentences = 5 , chars = 0 , auto_suggest = True , redirect = True ) 
             engine.say(respuestas)
             engine.runAndWait()
        
        if 'Reproduce' in entrada:
            Videos = entrada.replace('Reproduce', '')
            pywhatkit.playonyt(Videos)

        if 'hora' in entrada:
             hora = strftime('%H:%M %p')
             engine.say =('Son las '+hora)
             engine.runAndWait()





            



        else:
            
            respuesta = obtener_respuesta(entrada)


        
        print("Asistente: " + respuesta)

        
        engine.say(respuesta)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError as e:
        print("Error al solicitar los resultados del reconocimiento de voz; {0}".format(e))
