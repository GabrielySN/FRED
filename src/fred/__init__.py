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


    # ALTERNÂNCIA DE IDIOMA POR VOZ ---------------------------------------------------------------------------------

    if "mudar para espanhol" in comando or "cambiar a español" in comando or "switch to spanish" in comando:
        idioma_atual = 'es-ES'
        print("Idioma alterado para ESPANHOL.")
        return

    elif "mudar para português" in comando or "cambiar a portugués" in comando or "switch to portuguese" in comando:
        idioma_atual = 'pt-BR'
        print("Idioma alterado para PORTUGUÊS.")
        return

    elif "mudar para inglês" in comando or "cambiar a inglés" in comando or "switch to english" in comando:
            idioma_atual = 'en-US'
            print("Idioma alterado para INGLÊS.")
            return

    # COMANDOS EM PORTUGUÊS-----------------------------------------------------------------------------------------

    if idioma_atual == 'pt-BR':
        #comandos do google:
        if "abrir navegador" in comando or "abrir google" in comando:
            os.system("xdg-open https://google.com &")

        elif "nova aba" in comando:
             with teclado.pressed(Key.ctrl):
                  teclado.press('t')
                  teclado.release('t')

        elif "fechar aba" in comando:
             with teclado.pressed(Key.ctrl):
                  teclado.press('w')
                  teclado.release('w')

        elif "reabrir aba" in comando:
             with teclado.pressed(Key.ctrl, Key.shift):
                  teclado.press('t')
                  teclado.release('t')

        elif "proxima guia" in comando:
             with teclado.pressed(Key.ctrl):
                  teclado.press('tab')
                  teclado.release('tab')

        elif "guia anterior" in comando:
             with teclado.pressed(Key.ctrl, Key.shift):
                  teclado.press('tab')
                  teclado.release('tab')

        elif "nova janela" in comando:
             with teclado.pressed(Key.ctrl):
                  teclado.press('n')
                  teclado.release('n')

        elif "nova janela" in comando:
            with teclado.pressed(Key.ctrl, Key.shift):
                teclado.press('n')
                teclado.release('n')

        elif "abrir histórico" in comando:
             with teclado.pressed(Key.ctrl):
                teclado.press('h')
                teclado.release('h')

        elif "abrir download" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('j')
                teclado.release('j')

        
        elif "adcionar oas favoritos" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('d')
                teclado.release('d')

        elif "abrir gerenciador de favoritos" in comando:
            with teclado.pressed(Key.ctrl,Key.shift):
                teclado.press('o')
                teclado.release('o')

        elif "pesquisar uma palavra" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('f')
                teclado.release('f')

        elif "abrir ferramentas de desenvolvedor" in comando:
            with teclado.pressed(Key.ctrl,Key.shift):
                teclado.press('j')
                teclado.release('j')
            teclado.press('f12')
            teclado.release('f12')
        
        #comando gerais do computador: 
        #Linux   
        elif "abrir terminal" in comando or "abrir comandos" in comando:
            with teclado.pressed(Key.ctrl, Key.alt):
                teclado.press('t')
                teclado.release('t')

        elif "ativar tela cheia" or "desativar tela cheia"  in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press(Key.f11)
                teclado.release(Key.f11)
        
        elif "fechar janela" in comando or "fechar programa" in comando:
            with teclado.pressed(Key.alt):
                teclado.press(Key.f4)
                teclado.release(Key.f4)

        elif "renomear arquivo" or "renomear pasta" in comando:
            teclado.press(Key.f2)
            teclado.release(Key.f2)

        # Windows
        elif "mostrar área de trabalho" or "ocultar área de trabalho" in comando:
             with teclado.pressed(Key.win):
                  teclado.press('d')
                  teclado.release('d')

        elif "abrir explorador de arquivos" in comando:
             with teclado.pressed(Key.win):
                  teclado.press('e')
                  teclado.release('e')


        #Abos sistemas operacionais 
        elif "escrever" in comando:
            # Se disser "Escrever olá como vai", ele digita o que vem depois da palavra-chave
            texto_para_digitar = comando.replace("escrever", "").strip()
            teclado.type(texto_para_digitar)

        elif "copiar" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('c')
                teclado.release('c')
        
        elif "colar" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('v')
                teclado.release('v')
        
        elif "va para esquerda" in comando:
            teclado.press(Key.left)
            teclado.release(Key.left) 
        
        elif "va para direita" in comando:
            teclado.press(Key.right)
            teclado.release(Key.right)
        
        elif "va para baixo" in comando:
            teclado.press(Key.down)
            teclado.release(Key.down)
        
        elif "va para cima" in comando:
                teclado.press(Key.up)
                teclado.release(Key.up)

        elif "apagar tudo" in comando:
                    
            with teclado.pressed(Key.ctrl):
                teclado.press('a')
                teclado.release('a')
            time.sleep(0.1)  
            teclado.press(Key.backspace)
            teclado.release(Key.backspace)
                    
        elif "apagar" in comando:
            teclado.press(Key.backspace)
            teclado.release(Key.backspace)

        elif "desfazer" in comando:
             with teclado.pressed(Key.ctrl):
                  teclado.press('z')
                  teclado.release('z')

        elif "refazer" in comando:
             with teclado.pressed(Key.ctrl):
                  teclado.press('y')
                  teclado.release('y')

        elif "selecionar tudo" in comando:
             with teclado.pressed(Key.ctrl):
                  teclado.press('a')
                  teclado.release('a')
    
        elif "aumentar volume" in comando:
            os.system("amixer set Master 10%+")
            
        elif "diminuir volume" in comando:
            os.system("amixer set Master 10%-")
            
        elif "confirmar" in comando:
            teclado.press(Key.enter)
            teclado.release(Key.enter)

        elif "encerrar programa" in comando or "desligar" in comando:
            print("👋 Encerrando...")
            sys.exit()

    # COMANDOS EM ESPANHOL ----------------------------------------------------------------------------
  
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

        elif "copie" in comando:
             with teclado.pressed(Key.ctrl):
                teclado.press('c')
                teclado.release('c')

        elif "cole" in comando:
                 with teclado.pressed(Key.ctrl):
                    teclado.press('v')
                    teclado.release('v')

        elif "va para esquerda" in comando:
             teclado.press(Key.left)
             teclado.release(Key.left) 

        elif "va para direita" in comando:
                     teclado.press(Key.right)
                     teclado.release(Key.right)

        elif "va para baixo" in comando:
                     teclado.press(Key.down)
                     teclado.release(Key.down)

        elif "va para cima" in comando:
                     teclado.press(Key.up)
                     teclado.release(Key.up)

        elif "borrar todo" in comando:
                            
                        with teclado.pressed(Key.ctrl):
                            teclado.press('a')
                            teclado.release('a')
                        time.sleep(0.1)  
                        teclado.press(Key.backspace)
                        teclado.release(Key.backspace)

        elif "borrar" in comando:
                    teclado.press(Key.backspace)
                    teclado.release(Key.backspace)
            
        elif "subir volumen" in comando:
            os.system("amixer set Master 10%+")
            
        elif "bajar volumen" in comando:
            os.system("amixer set Master 10%-")
            
        elif "aceptar" in comando:
            teclado.press(Key.enter)
            teclado.release(Key.enter)

        elif "cerrar asistente" in comando or "apagar" in comando:
            print("👋 Saliendo...")
            sys.exit()

# COMANDOS EM INGLÊS--------------------------------------------------------------------------------------------------


def main() -> None:
    print("=== ASSISTENTE DE ACESSIBILIDADE TRILÍNGUE (LINUX) ===")
    while True:
        comando_voz = ouvir_microfone()
        executar_comando(comando_voz)