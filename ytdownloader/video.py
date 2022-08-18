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

        #Mostra as opções disponiveis
        # mostra_resolution()
        # #lê a opção escolhida pelo usuario.
        # op = resolution()

        #faz a verificação da opção do usuario.
        video = yt.streams.filter(res=resolução).first()

        #baixa o video em .mp4 na pasta videos
        video.download(cwd+"\\videos")

        print(Fore.LIGHTBLUE_EX+Style.BRIGHT+'O video foi baixado com sucesso!'+Fore.RESET+Style.RESET_ALL)
        sleep(5)
    except:
            popup('O URL digitado é invalido!')

#def esolha_de_resolution(op, yt, res):
# #    if op == 1:
        # video = yt.streams.get_highest_resolution()
    # else:
    #     if op == 2:
    #         res1 = "720p"
    #     elif op == 3:
    #         res1 = "480p"
    #     elif op == 4:
    #         res1 = "360p"
    #     elif op == 5:
    #         res1 = "240p"
    #     elif op == 6:
    #         res1 = "144p"
    #     video = yt.streams.filter(res=res1).first()
    # return video
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