import PySimpleGUI as sg
import hashlib

def hash_password(password):
    # Hash a password for storing.
    return hashlib.sha256(password.encode()).hexdigest()

# Dicionário contendo os usuários e hash das senhas
logins = dict()
logins['Cadu'] = 'b7e94be513e96e8c45cd23d162275e5a12ebde9100a425c4ebcdd7fa4dcd897c'

def tela_login():
    sg.theme('Reddit')
    Layout =[
        [sg.Text('Usuario'),sg.Input(key='Usuario')],
        [sg.Text('Senha'), sg.Input (key='Senha', password_char ='*')],
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
    if window == janela1:
        if eventos == sg.WIN_CLOSED:
            break
        if eventos == 'Entrar' and conf_login() == True:
            janela2 = tela_logado()
            janela1.close()
        if eventos == 'Entrar' and conf_login() != True:
            janela1.hide()
            janela3 = tela_recusado()
    if window == janela2:
        if eventos == 'OK':
            janela2.close()
            break
    if window == janela3:
        if eventos == 'Voltar':
            janela1.un_hide()
            janela3.close()
        if eventos == 'Fechar':
            janela3.close()
            break









