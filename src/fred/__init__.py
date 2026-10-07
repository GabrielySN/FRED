import speech_recognition as sr
from pynput.keyboard import Key, Controller as KeyboardController
import os
import sys
import time

# Inicializa o emulador de teclado
teclado = KeyboardController()

# Configuração global de idioma padrão
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

def executar_comando(comando):
    global idioma_atual
    if not comando:
        return

    # ==========================================
    # 🔄 ALTERNÂNCIA DE IDIOMA POR VOZ
    # ==========================================
    if "mudar para espanhol" in comando or "cambiar a español" in comando:
        idioma_atual = 'es-ES'
        print("🇨🇱🇪🇸 Idioma alterado para ESPANHOL.")
        return

    elif "mudar para português" in comando or "cambiar a portugués" in comando:
        idioma_atual = 'pt-BR'
        print("🇧🇷🇵🇹 Idioma alterado para PORTUGUÊS.")
        return

    # ==========================================
    # 🇧🇷 COMANDOS EM PORTUGUÊS
    # ==========================================
    if idioma_atual == 'pt-BR':
        
        if "abrir navegador" in comando or "abrir google" in comando:
            os.system("xdg-open https://google.com &")
            
        elif "abrir terminal" in comando or "abrir comandos" in comando:
            with teclado.pressed(Key.ctrl, Key.alt):
                teclado.press('t')
                teclado.release('t')
                
        elif "fechar janela" in comando or "fechar programa" in comando:
            with teclado.pressed(Key.alt):
                teclado.press(Key.f4)
                teclado.release(Key.f4)
                
        elif "escrever" in comando:
            # Se disser "Escrever olá como vai", ele digita o que vem depois da palavra-chave
            texto_para_digitar = comando.replace("escrever", "").strip()
            teclado.type(texto_para_digitar)
            
        elif "aumentar volume" in comando:
            os.system("amixer set Master 10%+")
            
        elif "diminuir volume" in comando:
            os.system("amixer set Master 10%-")
            
        elif "dar enter" in comando or "confirmar" in comando:
            teclado.press(Key.enter)
            teclado.release(Key.enter)

        elif "encerrar programa" in comando or "desligar assistente" in comando:
            print("👋 Encerrando...")
            sys.exit()

    # ==========================================
    # 🇪🇸 COMANDOS EM ESPANHOL
    # ==========================================
    elif idioma_atual == 'es-ES':
        
        if "abrir navegador" in comando or "abrir internet" in comando:
            os.system("xdg-open https://google.com &")
            
        elif "abrir terminal" in comando or "abrir comandos" in comando:
            with teclado.pressed(Key.ctrl, Key.alt):
                teclado.press('t')
                teclado.release('t')
                
        elif "cerrar ventana" in comando or "cerrar programa" in comando:
            with teclado.pressed(Key.alt):
                teclado.press(Key.f4)
                teclado.release(Key.f4)
                
        elif "escribir" in comando:
            texto_para_digitar = comando.replace("escribir", "").strip()
            teclado.type(texto_para_digitar)
            
        elif "subir volumen" in comando:
            os.system("amixer set Master 10%+")
            
        elif "bajar volumen" in comando:
            os.system("amixer set Master 10%-")
            
        elif "presionar enter" in comando or "aceptar" in comando:
            teclado.press(Key.enter)
            teclado.release(Key.enter)

        elif "cerrar asistente" in comando or "apagar" in comando:
            print("👋 Saliendo...")
            sys.exit()


def main() -> None:
    print("=== ASSISTENTE DE ACESSIBILIDADE BILÍNGUE (LINUX) ===")
    while True:
        comando_voz = ouvir_microfone()
        executar_comando(comando_voz)
