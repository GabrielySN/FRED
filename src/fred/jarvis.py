import speech_recognition as sr
from pynput.keyboard import Key, Controller as KeyboardController
import os
import sys
import time

def sair():
    print("Sai")

commandos = (
    {
        "function": sair,
        "palavras": ["encerrar programa", "fechar"]
    },
)

teclado = KeyboardController()
idioma_atual = 'pt-BR' 

def ouvir_microfone():
    global idioma_atual
    reconhecedor = sr.Recognizer()
    
    # Parâmetros de acessibilidade: ajusta os tempos para pessoas que falam mais pausadamente
    reconhecedor.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        reconhecedor.adjust_for_ambient_noise(source, duration=1)
        print(f"🎙️ [Idioma Ativo: {idioma_atual}] Ouvindo comando...")
        
        try:
            # Captura o áudio com margem de tempo confortável
            audio = reconhecedor.listen(source, timeout=6, phrase_time_limit=8)
            print("🤖 Processando voz...")
            
            # Reconhece no idioma que está ativo no momento
            comando = reconhecedor.recognize_google(audio, language=idioma_atual)
            print(f"🎙️ Escutado: \"{comando}\"")
            return comando.lower()
            
        except sr.UnknownValueError:
            print("❌ Áudio não reconhecido / Sonido no entendido.")
            return ""
        except sr.RequestError:
            print("❌ Erro de conexão com a internet / Error de red.")
            return ""
        except Exception:
            return ""

def findCommand(comando):
    for x in commandos:
        if x.get("palavras").index(comando.lower()) >= 0:
            return x

def executar_comando(comando):
    global idioma_atual
    if not comando:
        return  

    linha = findCommand(comando)
    if not linha:
        print("Comando não encontrado.")
        return

    funcao = linha.get("function")
    if callable(funcao):
        funcao()
    


def main() -> None:
    print("=== ASSISTENTE DE ACESSIBILIDADE BILÍNGUE (LINUX) ===")
    while True:
        comando_voz = ouvir_microfone()
        executar_comando(comando_voz)

main()