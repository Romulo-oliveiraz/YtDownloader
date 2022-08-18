def playlist_download(url):
    from colorama import Fore, Style
    from PySimpleGUI import popup
    try:
        from time import sleep
        from pytube import Playlist
        import os

        #url = str(input(Fore.MAGENTA+'Digite o URL da PlayList:'+Fore.RESET))

        p = Playlist(url)

        cwd = os.getcwd()

        #pega o nome da playlist é coloca na variavel
        nome_pasta = f"\playlist\{p.title}"
    
        print(Fore.LIGHTCYAN_EX+Style.BRIGHT+f'Baixando a playlist: {p.title}'+Fore.RESET+Style.RESET_ALL)

        for video1 in p.videos:
            video = video1.streams.get_audio_only()

            #baixa a musica em .mp4
            arquivo_baixado = video.download(cwd+nome_pasta)

            #seleciona a musica em .mp4 e converte ela para .mp3
            convert_to_mp3(arquivo_baixado)
            
            print(Fore.LIGHTBLUE_EX+Style.BRIGHT+f'A música {video1.title} foi baixada com sucesso!'+Fore.RESET+Style.RESET_ALL)

            sleep(5)
    except:
        
        popup('O URL digitado é invalido ou não é uma PlayList!')
def convert_to_mp3(arquivo_baixado):

    import os
    nome, ext = os.path.splitext(arquivo_baixado)
    #renomeia o arquivo colocando o .mp3 na frente
    novo_arquivo = nome + '.mp3'
    #renomeia o arquivo os.rename(<Atual nome do arquivo>, <Novo nome do arquivo.>)
    os.rename(arquivo_baixado, novo_arquivo)

if __name__ == '__main__':
    playlist_download()