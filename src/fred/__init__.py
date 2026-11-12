import speech_recognition as sr
from pynput.keyboard import Key, Controller as KeyboardController
import os
import sys
import time
import webbrowser
import subprocess
import shutil

# Inicializa o emulador de teclado
teclado = KeyboardController()

terminais = ["x-terminal-emulator", "gnome-terminal", "konsole", "xfce4-terminal", "xterm"]
terminal = next((t for t in terminais if shutil.which(t)), None)

# Configuração global de idioma padrão
idioma_atual = 'pt-BR' 

def ouvir_microfone():
    global idioma_atual
    reconhecedor = sr.Recognizer()
    
    # Parâmetros de acessibilidade: ajusta os tempos para pessoas que falam mais pausadamente
    reconhecedor.dynamic_energy_threshold = True
    # Padrão é 0.8. Com 2.0, você pode pausar por até 1 segundos entre as palavras.
    reconhecedor.pause_threshold = 1.0
    # Tempo de silêncio tolerado antes da fala começar
    reconhecedor.non_speaking_duration = 1.0
    
    with sr.Microphone() as source:
        reconhecedor.adjust_for_ambient_noise(source, duration=1)
        print(f"🎙️ [Idioma Ativo: {idioma_atual}] Ouvindo comando...")
        
        try:
            # Captura o áudio com margem de tempo confortável
            audio = reconhecedor.listen(source, timeout=6)
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

        elif "próxima guia" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press(Key.tab)
                teclado.release(Key.tab)

        elif "guia anterior" in comando:
            with teclado.pressed(Key.ctrl, Key.shift):
                teclado.press(Key.tab)
                teclado.release(Key.tab)

        elif "nova janela" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('n')
                teclado.release('n')

        elif "janela anônima" in comando:
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
        
        elif "adicionar aos favoritos" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('d')
                teclado.release('d')

        elif "gerenciador de favoritos" in comando:
            with teclado.pressed(Key.ctrl,Key.shift):
                teclado.press('o')
                teclado.release('o')

        elif "pesquisar palavra" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('f')
                teclado.release('f')

        elif "abrir ferramenta desenvolvedor" in comando:
            with teclado.pressed(Key.ctrl,Key.shift):
                teclado.press('j')
                teclado.release('j')
            teclado.press('f12')
            teclado.release('f12')

        elif "sair" in comando:
            teclado.press(Key.esc)
            teclado.release(Key.esc)

        elif "abrir gmail" in comando or "abrir email" in comando:
            webbrowser.open("https://mail.google.com/")

        elif "abrir sala" in comando or "abrir sala de aula" in comando:
            webbrowser.open("https://classroom.google.com/")

        elif "abrir youtube" in comando:
            webbrowser.open("https://www.youtube.com/")

        elif "abrir khan academy" in comando or "abrir khan" in comando:
            webbrowser.open("https://pt.khanacademy.org?/")

        elif "abrir redação" in comando:
            webbrowser.open("https://redacao.pr.gov.br")

        elif "abrir alura" in comando:
            webbrowser.open("https://cursos.alura.com.br/")

        elif "abrir matific" in comando:
            webbrowser.open("https://www.matific.com/")

        elif "abrir leia paraná" in comando:
            webbrowser.open("https://leiaparana.odilo.us/")

        elif "abrir inglês" in comando or "abrir inglês paraná" in comando:
            webbrowser.open("https://pt.englishcentral.com/")

        elif "abrir enem paraná" in comando or "abrir enem" in comando:
            webbrowser.open("https://enempr.com.br/")

        elif "abrir quizes" in comando:
            webbrowser.open("https://wayground.com/")

        elif "abrir documento" in comando:
            webbrowser.open("https://docs.google.com/")

        elif "lipar navegação" in comando or "limpar cache" in comando:
            with teclado.pressed(Key.ctrl, Key.shift):
                teclado.press(Key.delete)
                teclado.release(Key.delete)
                    
        #comando gerais do computador: 
        
        #Linux   
        
        elif "abrir terminal" in comando or "abrir comandos" in comando:
            subprocess.Popen([terminal])

        elif "tela cheia" in comando or "desativar tela cheia"  in comando:
            teclado.press(Key.f11)
            teclado.release(Key.f11)
        
        elif "renomear arquivo" in comando or "renomear pasta" in comando:
            teclado.press(Key.f2)
            teclado.release(Key.f2)

        elif "atualizar página" in comando:
            teclado.press(Key.f5)
            teclado.release(Key.f5)
        

        elif "opção de encerramento" in comando:
            with teclado.pressed(Key.ctrl, Key.alt):
                teclado.press(Key.delete)
                teclado.release(Key.delete)



        # Windows
        
        elif "mostrar área de trabalho" in comando or "ocultar área de trabalho" in comando:
            with teclado.pressed(Key.win):
                teclado.press('d')
                teclado.release('d')

        elif "abrir explorador de arquivos" in comando:
            with teclado.pressed(Key.win):
                teclado.press('e')
                teclado.release('e')

        elif "configurações w" in comando:
            with teclado.pressed(Key.win):
                teclado.press('i')
                teclado.release('i')

        elif "bloquear computador" in comando:
            with teclado.pressed(Key.win):
                teclado.press('l')
                teclado.release('l')

        elif "abrir gerenciador de tarefas" in comando:
            with teclado.pressed(Key.ctrl, Key.shift):
                teclado.press(Key.esc)
                teclado.release(Key.esc)

        

        #Abos sistemas operacionais
        
        elif "alterar janela" in comando:
            with teclado.pressed(Key.alt):
                teclado.press(Key.tab)
                teclado.release(Key.tab)
        
        elif "tirar print" in comando:
            teclado.press(Key.print_screen)
            teclado.release(Key.print_screen)

        elif "criar nova pasta" in comando:
            with teclado.pressed(Key.ctrl, Key.shift ):
                teclado.press('n')
                teclado.release('n')

        elif "fechar janela" in comando or "fechar programa" in comando:
            with teclado.pressed(Key.alt):
                teclado.press(Key.f4)
                teclado.release(Key.f4)
        
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
        
        elif "vá para esquerda" in comando:
            teclado.press(Key.left)
            teclado.release(Key.left) 
        
        elif "vá para direita" in comando:
            teclado.press(Key.right)
            teclado.release(Key.right)
        
        elif "vá para baixo" in comando:
            teclado.press(Key.down)
            teclado.release(Key.down)
        
        elif "vá para cima" in comando:
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

        elif "abrir vs code" in comando:
            os.system("code")
             
        elif "abrir calculadora" in comando:
            os.system("gnome-calculator &")

        elif "encerrar programa" in comando or "desligar" in comando:
            print("👋 Encerrando...")
            sys.exit()

    # COMANDOS EM ESPANHOL ----------------------------------------------------------------------------
    elif idioma_atual == 'es-ES':
        #comandos do google:
        if "abrir navegador" in comando or "abrir google" in comando:
            os.system("xdg-open https://google.com &")

        elif "nueva pestaña" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('t')
                teclado.release('t')

        elif "cerrar pestaña" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('w')
                teclado.release('w')

        elif "reabrir pestaña" in comando:
            with teclado.pressed(Key.ctrl, Key.shift):
                teclado.press('t')
                teclado.release('t')

        elif "próxima guía" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press(Key.tab)
                teclado.release(Key.tab)

        elif "guía anterior" in comando:
            with teclado.pressed(Key.ctrl, Key.shift):
                teclado.press(Key.tab)
                teclado.release(Key.tab)

        elif "nueva ventana" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('n')
                teclado.release('n')

        elif "ventana anónima" in comando:
            with teclado.pressed(Key.ctrl, Key.shift):
                teclado.press('n')
                teclado.release('n')

        elif "abrir historial" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('h')
                teclado.release('h')

        elif "abrir descarga" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('j')
                teclado.release('j')
        
        elif "añadir a favoritos" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('d')
                teclado.release('d')

        elif "gestor de  favoritos" in comando:
            with teclado.pressed(Key.ctrl,Key.shift):
                teclado.press('o')
                teclado.release('o')

        elif "buscar palabra" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('f')
                teclado.release('f')

        elif "abrir herramientas de desarrollador" in comando:
            with teclado.pressed(Key.ctrl,Key.shift):
                teclado.press('j')
                teclado.release('j')
            teclado.press('f12')
            teclado.release('f12')

        elif "salir" in comando:
            teclado.press(Key.esc)
            teclado.release(Key.esc)

        elif "abrir gmail" in comando or "abrir correo electrónico" in comando:
            webbrowser.open("https://mail.google.com/")

        elif "abrir habitación" in comando:
            webbrowser.open("https://classroom.google.com/")

        elif "abrir youtube" in comando:
            webbrowser.open("https://www.youtube.com/")

        elif "abrir khan academy" in comando or "abrir khan" in comando:
            webbrowser.open("https://pt.khanacademy.org?/")

        elif "abrir redacción" in comando:
            webbrowser.open("https://redacao.pr.gov.br")

        elif "abrir alura" in comando:
            webbrowser.open("https://cursos.alura.com.br/")

        elif "abrir matific" in comando:
            webbrowser.open("https://www.matific.com/")

        elif "abrir leia paraná" in comando:
            webbrowser.open("https://leiaparana.odilo.us/")

        elif "abrir inglés" in comando or "abrir inglés paraná" in comando:
            webbrowser.open("https://pt.englishcentral.com/")

        elif "abrir enem paraná" in comando or "abrir enem" in comando:
            webbrowser.open("https://enempr.com.br/")

        elif "abrir quizes" in comando:
            webbrowser.open("https://wayground.com/")

        elif "abrir documento" in comando:
            webbrowser.open("https://docs.google.com/")

        elif "limpiar navegación" in comando or "limpiar caché" in comando:
            with teclado.pressed(Key.ctrl, Key.shift):
                teclado.press(Key.delete)
                teclado.release(Key.delete)
                    
        #comando gerais do computador: 
        
        #Linux   
        
        elif "abrir terminal" in comando or "abrir comandos" in comando:
            subprocess.Popen([terminal])

        elif "pantalla completa" in comando or "desactivar pantalla completa"  in comando:
            teclado.press(Key.f11)
            teclado.release(Key.f11)
        
        elif "renombrar archivo" in comando or "renombrar carpeta" in comando:
            teclado.press(Key.f2)
            teclado.release(Key.f2)

        elif "actualizar página" in comando:
            teclado.press(Key.f5)
            teclado.release(Key.f5)

        elif "opción de cierre" in comando:
            with teclado.pressed(Key.ctrl, Key.alt):
                teclado.press(Key.delete)
                teclado.release(Key.delete)



        # Windows
        
        elif "mostrar escritorio" in comando or "ocultar el escritorio" in comando:
            with teclado.pressed(Key.win):
                teclado.press('d')
                teclado.release('d')

        elif "abrir el explorador de archivos" in comando:
            with teclado.pressed(Key.win):
                teclado.press('e')
                teclado.release('e')

        elif "configuraciones w" in comando:
            with teclado.pressed(Key.win):
                teclado.press('i')
                teclado.release('i')

        elif "bloquear computador" in comando:
            with teclado.pressed(Key.win):
                teclado.press('l')
                teclado.release('l')

        elif "abrir el administrador de tareas" in comando:
            with teclado.pressed(Key.ctrl, Key.shift):
                teclado.press(Key.esc)
                teclado.release(Key.esc)

        

        #Abos sistemas operacionais
        
        elif "modificar ventana" in comando:
            with teclado.pressed(Key.alt):
                teclado.press(Key.tab)
                teclado.release(Key.tab)
        
        elif "tomar una captura de pantalla" in comando:
            teclado.press(Key.print_screen)
            teclado.release(Key.print_screen)

        elif "crear nueva carpeta" in comando:
            with teclado.pressed(Key.ctrl, Key.shift ):
                teclado.press('n')
                teclado.release('n')

        elif "cerrar ventana" in comando or "cerrar programa" in comando:
            with teclado.pressed(Key.alt):
                teclado.press(Key.f4)
                teclado.release(Key.f4)
        
        elif "escribir" in comando:
            # Se disser "Escrever olá como vai", ele digita o que vem depois da palavra-chave
            texto_para_digitar = comando.replace("escrever", "").strip()
            teclado.type(texto_para_digitar)

        elif "copiar" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('c')
                teclado.release('c')
        
        elif "pegar" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('v')
                teclado.release('v')
        
        elif "ve a la izquierda" in comando:
            teclado.press(Key.left)
            teclado.release(Key.left) 
        
        elif "ve a la derecha" in comando:
            teclado.press(Key.right)
            teclado.release(Key.right)
        
        elif "ve hacia abajo" in comando:
            teclado.press(Key.down)
            teclado.release(Key.down)
        
        elif "ve hacia arriba" in comando:
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

        elif "deshacer" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('z')
                teclado.release('z')

        elif "rehacer" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('y')
                teclado.release('y')

        elif "seleccionar todo" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('a')
                teclado.release('a')
    
        elif "aumentar el volumen" in comando:
            os.system("amixer set Master 10%+")
            
        elif "disminuir el volumen" in comando:
            os.system("amixer set Master 10%-")
            
        elif "confirmar" in comando:
            teclado.press(Key.enter)
            teclado.release(Key.enter)

        elif "abrir vs code" in comando:
            os.system("code")
                
        elif "abrir calculadora" in comando:
            os.system("gnome-calculator &")

        elif "cerrar programa" in comando or "apagar" in comando:
            print("👋 Finalizando...")
            sys.exit()
                

    # COMANDOS EM INGLÊS--------------------------------------------------------------------------------------------------
    elif idioma_atual == 'en-US':

        #comandos do google:
        if "open browser" in comando or "open google" in comando:
            os.system("xdg-open https://google.com &")

        elif "new tab" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('t')
                teclado.release('t')

        elif "close tab" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('w')
                teclado.release('w')

        elif "reopen tab" in comando:
            with teclado.pressed(Key.ctrl, Key.shift):
                teclado.press('t')
                teclado.release('t')

        elif "next tab" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press(Key.tab)
                teclado.release(Key.tab)

        elif "previous guide" in comando:
            with teclado.pressed(Key.ctrl, Key.shift):
                teclado.press(Key.tab)
                teclado.release(Key.tab)

        elif "new window" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('n')
                teclado.release('n')

        elif "incognito window" in comando:
            with teclado.pressed(Key.ctrl, Key.shift):
                teclado.press('n')
                teclado.release('n')

        elif "open history" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('h')
                teclado.release('h')

        elif "open download" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('j')
                teclado.release('j')
        
        elif "add to favorites" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('d')
                teclado.release('d')

        elif "bookmark manager" in comando:
            with teclado.pressed(Key.ctrl,Key.shift):
                teclado.press('o')
                teclado.release('o')

        elif "search for a word" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('f')
                teclado.release('f')

        elif "open developer tool" in comando:
            with teclado.pressed(Key.ctrl,Key.shift):
                teclado.press('j')
                teclado.release('j')
            teclado.press('f12')
            teclado.release('f12')

        elif "exit" in comando:
            teclado.press(Key.esc)
            teclado.release(Key.esc)

        elif "open gmail" in comando or "open email" in comando:
            webbrowser.open("https://mail.google.com/")

        elif "open room" in comando or "open classroom" in comando:
            webbrowser.open("https://classroom.google.com/")

        elif "open youtube" in comando:
            webbrowser.open("https://www.youtube.com/")

        elif "open khan academy" in comando or "open khan" in comando:
            webbrowser.open("https://pt.khanacademy.org?/")

        elif "open essay" in comando:
            webbrowser.open("https://redacao.pr.gov.br")

        elif "open alura" in comando:
            webbrowser.open("https://cursos.alura.com.br/")

        elif "open matific" in comando:
            webbrowser.open("https://www.matific.com/")

        elif "open leia paraná" in comando:
            webbrowser.open("https://leiaparana.odilo.us/")

        elif "open english" in comando or "Open english paraná" in comando:
            webbrowser.open("https://pt.englishcentral.com/")

        elif "open enem paraná" in comando or "open enem" in comando:
            webbrowser.open("https://enempr.com.br/")

        elif "open quizzes" in comando:
            webbrowser.open("https://wayground.com/")

        elif "open document" in comando:
            webbrowser.open("https://docs.google.com/")

        elif "clear navigation" in comando or "clear cache" in comando:
            with teclado.pressed(Key.ctrl, Key.shift):
                teclado.press(Key.delete)
                teclado.release(Key.delete)
                    
        #comando gerais do computador: 
        
        #Linux   
        
        elif "open terminal" in comando or "open commands" in comando:
            subprocess.Popen([terminal])

        elif "full screen" in comando or "disable full screen "  in comando:
            teclado.press(Key.f11)
            teclado.release(Key.f11)
        
        elif "rename file" in comando or "rename folder" in comando:
            teclado.press(Key.f2)
            teclado.release(Key.f2)

        elif "refresh page" in comando:
            teclado.press(Key.f5)
            teclado.release(Key.f5)

        elif "termination option" in comando:
            with teclado.pressed(Key.ctrl, Key.alt):
                teclado.press(Key.delete)
                teclado.release(Key.delete)



        # Windows
        
        elif "show desktop" in comando or "hide desktop" in comando:
            with teclado.pressed(Key.win):
                teclado.press('d')
                teclado.release('d')

        elif "open file explorer" in comando:
            with teclado.pressed(Key.win):
                teclado.press('e')
                teclado.release('e')

        elif "w settings" in comando:
            with teclado.pressed(Key.win):
                teclado.press('i')
                teclado.release('i')

        elif "lock computer" in comando:
            with teclado.pressed(Key.win):
                teclado.press('l')
                teclado.release('l')

        elif "open task manager" in comando:
            with teclado.pressed(Key.ctrl, Key.shift):
                teclado.press(Key.esc)
                teclado.release(Key.esc)


        #Abos sistemas operacionais
        
        elif "change window" in comando:
            with teclado.pressed(Key.alt):
                teclado.press(Key.tab)
                teclado.release(Key.tab)
        
        elif "take a screenshot" in comando:
            teclado.press(Key.print_screen)
            teclado.release(Key.print_screen)

        elif "create new folder" in comando:
            with teclado.pressed(Key.ctrl, Key.shift ):
                teclado.press('n')
                teclado.release('n')

        elif "close window" in comando or "close program" in comando:
            with teclado.pressed(Key.alt):
                teclado.press(Key.f4)
                teclado.release(Key.f4)
        
        elif "write" in comando:
            # Se disser "Escrever olá como vai", ele digita o que vem depois da palavra-chave
            texto_para_digitar = comando.replace("escrever", "").strip()
            teclado.type(texto_para_digitar)

        elif "copy" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('c')
                teclado.release('c')
        
        elif "to paste" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('v')
                teclado.release('v')
        
        elif "go to the left" in comando:
            teclado.press(Key.left)
            teclado.release(Key.left) 
        
        elif "go to the right" in comando:
            teclado.press(Key.right)
            teclado.release(Key.right)
        
        elif "go down" in comando:
            teclado.press(Key.down)
            teclado.release(Key.down)
        
        elif "go up" in comando:
            teclado.press(Key.up)
            teclado.release(Key.up)

        elif "delete everything" in comando:
                    
            with teclado.pressed(Key.ctrl):
                teclado.press('a')
                teclado.release('a')
            time.sleep(0.1)  
            teclado.press(Key.backspace)
            teclado.release(Key.backspace)
                    
        elif "delete" in comando:
            teclado.press(Key.backspace)
            teclado.release(Key.backspace)

        elif "undo" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('z')
                teclado.release('z')

        elif "redo" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('y')
                teclado.release('y')

        elif "select all" in comando:
            with teclado.pressed(Key.ctrl):
                teclado.press('a')
                teclado.release('a')
    
        elif "increase volume" in comando:
            os.system("amixer set Master 10%+")
            
        elif "decrease volume" in comando:
            os.system("amixer set Master 10%-")
            
        elif "confirm" in comando:
            teclado.press(Key.enter)
            teclado.release(Key.enter)

        elif "open vs code" in comando:
            os.system("code")
                
        elif "open calculator" in comando:
            os.system("gnome-calculator &")

        elif "close" in comando or "turn off" in comando:
            print("👋 Closing...")
            sys.exit()

def main() -> None:
    print("=== ASSISTENTE DE ACESSIBILIDADE TRILÍNGUE (LINUX) ===")
    while True:
        comando_voz = ouvir_microfone()
        executar_comando(comando_voz)