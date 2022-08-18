from colorama import Fore, Style
from PySimpleGUI import popup
def down_video(url, res1):
    try:
        from time import sleep
        from pytube.cli import on_progress
        from pytube import YouTube
        import os

        #url = str(input(Fore.MAGENTA+'Digite o URL do video:'+Fore.RESET))

        cwd = os.getcwd()

        #pega a url do video.
        link = url
        resolução = f"{res1}"

        #Pega o video na melhor qualidade disponivel.
        yt = YouTube(link, on_progress_callback=on_progress)

        #faz a verificação da opção do usuario.
        video = yt.streams.filter(res=resolução).first()

        #baixa o video em .mp4 na pasta videos
        video.download(cwd+"\\videos")

        popup('O video foi baixado com sucesso!')
    except:
            popup('O URL digitado é invalido!')

def resolution():  
    op = int(input(Fore.MAGENTA+'Qual resolução você deseja baixar?'+Fore.RESET))
    while op not in (1,2,3,4,5,6):
        print(Fore.RED+Style.BRIGHT+'Valor invalido!!'+Fore.RESET+Style.RESET_ALL)
        op = int(input(Fore.MAGENTA+'Qual resolução você deseja baixar?'+Fore.RESET))
    return op

def mostra_resolution():
    print(Fore.GREEN+"""OPÇÕES:
    [ 1 ] = [Melhor resolução possivel]
    [ 2 ] = [720p]
    [ 3 ] = [480p]
    [ 4 ] = [360p]
    [ 5 ] = [240p]
    [ 6 ] = [144p]
    """+Fore.RESET)

if __name__ == '__main__':
    down_video()