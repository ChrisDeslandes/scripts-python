from __future__ import unicode_literals
import youtube_dl
from pathlib import Path
import os
from colorama import init, Style, Fore

def Saudacao():
    init()
    print(Style.BRIGHT)
    print("--- " + Fore.CYAN + "Bem-vindo ao seu programa de download de vídeos e músicas" + Fore.RESET + " ---\n\n\n")
    PrimeiroMenu()

def PrimeiroMenu():
    while 1:
        global ydl_opts, ext, pasta
        ydl_opts = {"ignore-errors": True, "continue": True}
        videoOuMusica = input("Deseja baixar vídeos ou músicas (V para vídeos, M para músicas)? ")
        if str(videoOuMusica).upper().replace(" ","") == "V":
            ydl_opts["format"] = "bestvideo+bestaudio"
            pasta = home.replace("\\","/") + "/Videos/"
            ext = "mp4"
            break
        elif str(videoOuMusica).upper().replace(" ","") == "M":
            ydl_opts["format"] = "bestaudio"
            pasta = home.replace("\\","/") + "/Music/"
            ext = "mp3"
            break
        else:
            print("Opção inválida!\n")
        print("")
    SegundoMenu()

def SegundoMenu():
    while 1:
        print()
        print("O que deseja?\n")
        print("1 - Baixar um arquivo")
        print("2 - Baixar arquivos a partir de um arquivo texto")
        print("3 - Baixar todos os arquivos de uma playlist do YouTube")
        print("4 - Baixar todos os arquivos de um canal do YouTube")
        global opcao
        opcao = input("\nDigite a opção desejada: ")
        if str(opcao).replace(" ","") == "1" or str(opcao).replace(" ","") == "2" or str(opcao).replace(" ","") == "3" or str(opcao).replace(" ","") == "4":
            opcao = str(opcao).replace(" ","")
            break
        else:
            print("Opção inválida!\n")
    Programa()

def Programa():    
    print()
    arqVetor = []
    if opcao == "1":
        arq = input("Digite o endereço completo do arquivo a ser baixado: ")
        print()
        arqVetor.append(arq)
        ydl_opts["outtmpl"] = home.replace("\\","/") + "/desktop/Músicas/%(title)s." + ext
    elif opcao == "2":
        while 1:
            arqTXT = input("Digite o endereço completo do arquivo .txt que contém o link dos arquivos: ")
            if os.path.exists(arqTXT):
                print("\n")
                f = open(arqTXT, "r")
                arq = f.read()
                f.close()
                arqVetor = arq.splitlines()
                ydl_opts["outtmpl"] = home.replace("\\","/") + "/downloads/Músicas/%(title)s." + ext
                break
            else:
                print("Este arquivo não existe!\n")
    elif opcao == "3":
        arq = input("Digite o endereço completo da PLAYLIST do Youtube: ")
        print()
        arqVetor.append(arq)
        ydl_opts["outtmpl"] = home.replace("\\","/") + "/desktop/Músicas/%(playlist_index)s - %(title)s." + ext
    else:
        arq = input("Digite o endereço completo do CANAL do Youtube: ").replace(" ","")
        print()
        arqVetor.append(arq)
        ydl_opts["outtmpl"] = home.replace("\\","/") + "/desktop/Músicas/%(title)s." + ext

    print("Baixando:\n")
    for i in arqVetor:
        print(i)

    print()
    try:
        youtube_dl.YoutubeDL(ydl_opts).download(arqVetor)
    except:
        pass

    print("\nCaso não tenha ocorrido um erro, as músicas foram salvas na pasta:\n" + home.replace("\\","/") + "/Desktop/Músicas\n\n")
    while 1:
        repetir = input("Deseja fazer outro download (S para Sim, N para Não)? ").replace(" ","").upper()
        if repetir == "S":
            print("\n\n-------------------------------------------------------------------------------------\n")
            PrimeiroMenu()
            break
        elif repetir == "N":
            break


home = str(Path.home())
ext = ""
pasta = ""
opcao = ""
ydl_opts = {}
Saudacao()
