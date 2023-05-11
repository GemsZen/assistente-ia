import speech_recognition as sr
import pyaudio
import webbrowser
import os
import subprocess
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import schedule
import time
import tkinter as tk
import threading

# Inicializando a biblioteca de reconhecimento de voz
audio = sr.Recognizer()
maquina = pyttsx3.init()

# Função para falar
def speak(text):
    maquina.say(text)
    maquina.runAndWait()
    
    
import subprocess

def atualizar_codigo():
    subprocess.call("git pull", shell=True) # Executa o comando git pull para atualizar o código do repositório local
    subprocess.call("python programa.py", shell=True) # Reinicia o programa após a atualização do código


def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'tina' in comando:
                comando = comando.replace('tina', '')
                maquina.say(comando)
                maquina.runAndWait()


    except:
        print('Microfone não está ok')

    return comando

# criar janela
janela = tk.Tk()
janela.title("Minha IA")

# criar botão para executar a IA
executar_button = tk.Button(janela, text="Ouvir", command=executa_comando)
executar_button.pack()

# criar rótulo para exibir o resultado da IA
resultado_label = tk.Label(janela, text="")
resultado_label.pack()

# iniciar a janela
janela.mainloop()


def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()

    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()

    elif 'toque' in comando:
        musica = comando.replace('toque','')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando música')
        maquina.runAndWait()

    elif "pesquisar" in comando:
        search_term = comando.replace("pesquisar", "")
        webbrowser.open(f"https://www.google.com/search?q={search_term}")

    elif 'atualizar código' in comando:
        maquina.say('Iniciando atualização de código')
        maquina.runAndWait()
        atualizar_codigo()   

    elif "abrir bloco de notas" in comando:
        subprocess.Popen("notepad.exe")

    elif "abrir battle net" in comando:
        os.startfile("C:/Program Files (x86)/Battle.net/Battle.net Launcher.exe")

    elif "abrir epic game" in comando:
        os.startfile("D:\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe")

    elif "aumentar volume" in comando:
        set_volume(comando)

    elif "diminuir volume" in comando:
        set_volume(comando)

    elif "abrir vscode" in comando:
        os.startfile("C:/Program Files/Microsoft VS Code/Code.exe")

    elif "abrir pycharm" in comando:
        os.startfile("C:/Program Files/JetBrains/PyCharm Community Edition 2021.1.1/bin/pycharm64.exe")

    elif "abrir explorador de arquivos" in comando:
        os.startfile("explorer.exe")

    elif "abrir discord ptb" in comando:
        os.startfile("C:/Users/[seu usuario]/AppData/Local/DiscordPTB/app-1.0.64/DiscordPTB.exe")

    elif "abrir spotify" in comando:
        os.startfile("C:/Users/Usuario/AppData/Roaming/Spotify/Spotify.exe")

    elif "abrir epic games" in comando:
        os.startfile("com.epicgames.launcher://apps/9773aa1aa54f4f7b80e44bef04986cea%3A530145df28a24424923f5828cc9031a1%3ASugar?action=launch&silent=true")
 
    elif "tocar" in comando:
        song_name = comando.replace("tocar", "")
        play_song(song_name)

    elif "desenhar" in comando:
        draw()

    elif "escrever" in comando:
        write()

# Função para ajustar o volume
def set_volume(command):
    if "aumentar volume" in command:
        amount = int(command.replace("aumentar volume em", "").replace("%", ""))
        subprocess.call(f'nircmd.exe setsysvolume +{amount}%')

    elif "diminuir volume" in command:
        amount = int(command.replace("diminuir volume em", "").replace("%", ""))
        subprocess.call(f'nircmd.exe setsysvolume -{amount}%')

# Função para tocar música no Spotify
def play_song(song_name):
    os.system(f'spotify play {song_name}')

# Função para desenhar
def draw():
    print("Digite as dimensões do desenho:")
    width = int(input("Largura: "))
    height = int(input("Altura: "))
    print(f"Desenhando na tela com dimensões {width}x{height}")

# Função para escrever
def write():
    print("Digite o que deseja escrever:")
    text = input()
    print(f"Escrevendo na tela: {text}")

comando_voz_usuario()
