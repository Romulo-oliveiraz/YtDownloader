def music(url):
    from colorama import Fore, Style
    from PySimpleGUI import popup
    try:
        from pytube.cli import on_progress
        from pytube import YouTube
        import os

        #url = str(input(Fore.MAGENTA+'Digite o URL da música:'+Fore.RESET))
        cwd = os.getcwd()

        #pega a url da musica.
        link = url

        #filtra para pegar somente o audio do video.
        yt = YouTube(link, on_progress_callback=on_progress)
        video = yt.streams.get_audio_only()

        #baixa a musica em .mp4
        arquivo_baixado = video.download(cwd+"\musicas")

        #seleciona a musica em .mp4 e converte ela para .mp3
        convert_to_mp3(arquivo_baixado)
        popup('A música foi baixada com sucesso!')

    except FileExistsError:
        popup('Essa música já foi baixada!')
        os.remove(arquivo_baixado)
    except:
        popup('O URL digitado é invalido, verifique se o video está disponivel!')   

    

##########################################
def convert_to_mp3(arquivo_baixado):

    import os
    nome, ext = os.path.splitext(arquivo_baixado)
    #renomeia o arquivo colocando o .mp3 na frente

    novo_arquivo = nome + '.mp3'
    #renomeia o arquivo os.rename(<Atual nome do arquivo>, <Novo nome do arquivo.>)

    os.rename(arquivo_baixado, novo_arquivo)


if __name__ == '__main__':
    music()