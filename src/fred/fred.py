import seepch_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Diga algo!")
    audio = r.listten(source)


try:
    print("Voce disse:" + r.recognize_google(audio, language="pt-BR"))
except sr.UnkonoWnValueError:
    print("FRED nao pode encontrar o audio")
except sr.RequestError as e:
    print("Erro ao chamr Google Speech Recognition service;{0}".format(e))
