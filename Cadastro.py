import PySimpleGUI as sg

#layout

def tela_login():
    sg.theme('Reddit')
    Layout =[
        [sg.Text('Usuario'),sg.Input(key='Usuario')],
        [sg.Text('Senha'), sg.Input (key='Senha',password_char ='*')],
        [sg.Checkbox ('Salvar login?')],
        [sg.Button('Entrar')],
    ]
    return sg.Window('login', layout= Layout, finalize=True)


def tela_logado():
    sg.theme('Reddit')
    Layout = [
        [sg.Text('LOGADO')],
        [sg.Button('OK')],
    ]
    return sg.Window('LOGADO', layout= Layout, finalize=True)

def tela_recusado():
    sg.theme('Reddit')
    Layout = [
        [sg.Text('RECUSADO')],
        [sg.Button('Voltar')],
        [sg.Button('Fechar')],
    ]
    return sg.Window ('RECUSADO', layout=Layout, finalize=True)

janela1, janela2, janela3 = tela_login(), None, None


def conf_login ():
    if valores['Usuario'] == 'Cadu' and valores['Senha'] == 'senha':
        return True


while True :
    window, eventos, valores = sg.read_all_windows()
    if window == janela1 and eventos == sg.WIN_CLOSED:
        break
    if window == janela1 and eventos =='Entrar' and conf_login() == True:
        janela2 = tela_logado()
        janela1.close()
    if window == janela2 and eventos == 'OK':
        janela2.close()
    if window == janela1 and eventos == 'Entrar' and conf_login() != True:
        janela1.hide()
        janela3 = tela_recusado()
    if window == janela3 and eventos =='Voltar':
        janela1.un_hide()
        janela3.close()
    if window == janela3 and eventos =='Fechar':
        janela3.close()








