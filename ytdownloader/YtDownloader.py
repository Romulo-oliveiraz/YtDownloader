
import main
import PySimpleGUI as sg
def tela_inicial():
    sg.theme('Dark')   # Add a little color to your windows
    layout = [  
        [sg.Text('Selecione o tipo de música que deseja baixar:')],
        [sg.Checkbox('Video', key='video'), sg.Checkbox('Música', key='musica'), sg.Checkbox('Playlist', key='playlist')],
        [sg.Text('Digite o URL'), sg.InputText(key='url')],
        [sg.Button('Baixar'), sg.Button('Sair', key='sair')]
        ]
    return sg.Window('Inicial', layout=layout, finalize=True)

def tela_video():
    sg.theme('Dark')   # Add a little color to your windows
    layout = [  
        [sg.Text('Deseja baixar o video em qual resolução?')],
        [sg.Checkbox('720p', key='720p'), 
        sg.Checkbox('480p', key='480p'), 
        sg.Checkbox('360p', key='360p'), 
        sg.Checkbox('240p', key='240p'), 
        sg.Checkbox('144p', key='144p')],
        [sg.Button('Baixar Video', key='video down'), sg.Button('Voltar', key='voltar')]

        ]
    return sg.Window('Resolução', layout=layout, finalize=True)

janela1, janela2 = tela_inicial(), None

def voltar(flag):
    janela1.un_hide()
    janela2.close()
    flag = True
    return flag

while True:

    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Baixar':
        
        if values['musica']:
            main.music(values['url'])

        elif values['playlist']:
            main.playlist_download(values['url'])

        if values['video'] == True:
            janela2 = tela_video()
            janela1.hide()
            flag = False
            while not flag:
                event2, values2 = janela2.read()
                if event2 == sg.WIN_CLOSED:
                    flag = True
                if event2 == 'voltar':
                    flag = voltar(flag)
                if event2 == 'video down':
                    if values2['720p'] == True:
                        main.down_video(values['url'], "720p")
                        
                    elif values2['480p'] == True:
                        main.down_video(values['url'], '480p')
                        
                    elif values2['360p'] == True:
                        main.down_video(values['url'], '360p')
                        
                    elif values2['240p'] == True:
                        main.down_video(values['url'], '240p')
                
                    elif values2['144p'] == True:
                        main.down_video(values['url'], '144p')
                    flag = voltar(flag)
    elif window == janela1 and event == 'sair':
        break                                      
