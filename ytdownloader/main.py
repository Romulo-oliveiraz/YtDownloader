
##########################################
from musica import music
from playlist import playlist_download
from video import down_video
from time import sleep
from colorama import Fore, Style
##########################################
def leiaint(msg):
    #define o valor em 0
    valor = 0
    #define a flag em falso
    flag = False
    #verifica se o valor digitado é um numero.
    while True:
        #importa um valor em forma de string
        n = str(input(Fore.BLUE+msg+Fore.RESET)).strip()
        #verifica se o valor é um numero inteiro
        if n.isnumeric():
            valor = int(n)
            if valor in (1,2,3):
                flag = True
        #para a repetição se o valor for um num
        if flag == True:
            break
        #continua a repetição até que seja digitado um valor valido
        else:
            print(Fore.RED+Style.BRIGHT+'ERROR! Digite somente os números 1, 2 ou 3!'+Fore.RESET+Style.RESET_ALL)

    return valor
##########################################
def select_op():
    opção = leiaint('Digite a opção desejada: ')
    return opção
##########################################
def mostra_opções():
    print(Fore.GREEN + """OPÇÕES:
    [ 1 ] = [Baixar Video]
    [ 2 ] = [Baixar Música]
    [ 3 ] = [Baixar Playlist]
    """+Fore.RESET)
##########################################
def escolha():
    #Lê a opção selecionada pelo usuario
    opção = select_op()
    #verifica a opção do usuario
    #executa a função de baixar video
    if opção == 1:
        res1= '144p'
        url = str(input(Fore.MAGENTA+'Digite o URL da PlayList:'+Fore.RESET))
        down_video(url, res1)
    #executa a função de baixar música
    elif opção == 2:
        url = str(input(Fore.MAGENTA+'Digite o URL da PlayList:'+Fore.RESET))
        music(url)
    #executa a função de baixar playlist
    elif opção == 3:
        url = str(input(Fore.MAGENTA+'Digite o URL da PlayList:'+Fore.RESET))
        playlist_download(url)
##########################################
def executa():
    import os
    while True:
        mostra_opções()
        escolha()
        sleep(5)
        os.system("cls")
        continuar = cond()
        if continuar == 'N':
            break
##########################################
def cond():
    continuar = str(input(Fore.MAGENTA+'Deseja baixar algo mais?[S/N]'+Fore.RESET)).upper().strip()
    while continuar not in 'SsNn':
        print(Fore.RED+Style.BRIGHT+'valor invalido digite somente [S/N]!'+Fore.RESET+Style.RESET_ALL)
        continuar = str(input(Fore.MAGENTA+'Deseja baixar algo mais?[S/N]'+Fore.RESET)).upper().strip()
    return continuar

if __name__ == '__main__':
    executa()
##########################################
