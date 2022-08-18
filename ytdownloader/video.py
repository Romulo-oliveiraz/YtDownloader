from colorama import Fore, Style
from PySimpleGUI import popup
def down_video(url, res1):
    try:
        from pytube.cli import on_progress
        from pytube import YouTube
        import os
 
        cwd = os.getcwd()

        #pega a url do video.
        link = url
        resolução = f"{res1}"

        #Pega o video na melhor qualidade disponivel.
        yt = YouTube(link, on_progress_callback=on_progress)
        streams = set()

        for stream in yt.streams.filter(type="video"):  # Only look for video streams to avoid None values
            streams.add(stream.resolution)
        #faz a verificação da opção do usuario.
        if res1 not in streams:
            popup('A resolução escolhida não está disponivel, será baixada a maior resolução!')
            video = yt.streams.get_highest_resolution()
        else:   
            video = yt.streams.filter(res=resolução).first()

        #baixa o video em .mp4 na pasta videos
        video.download(cwd+"\\videos")

        popup('O video foi baixado com sucesso!')
    except:
        popup('O URL digitado é invalido!')

if __name__ == '__main__':
    down_video()