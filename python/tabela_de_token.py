# Defina os tipos de tokens como constantes
TOKEN_PROGRAMA_SOL = 'PROGRAMA_SOL'
TOKEN_LOOP = 'LOOP'
TOKEN_VEZES = 'VEZES'
TOKEN_SEQUENCIA = 'SEQUENCIA'
TOKEN_PRESENT = 'PRESENT'
TOKEN_TEMPO = 'TEMPO'
TOKEN_FASES_EPIC = 'FASES_EPIC'
TOKEN_EXPLORE = 'EXPLORE'
TOKEN_NAVEGAR = 'NAVEGAR'
TOKEN_VISUALIZAR_PDF = 'VISUALIZAR_PDF'
TOKEN_VISUALIZAR_VIDEO = 'VISUALIZAR_VIDEO'
TOKEN_VIDEOCONFERENCIA = 'VIDEOCONFERENCIA'
TOKEN_INTERACT = 'INTERACT'
TOKEN_WHATSAPP_WEB = 'WHATSAPP_WEB'
TOKEN_EMAIL = 'EMAIL'
TOKEN_CRITIQUE = 'CRITIQUE'
TOKEN_VEZES_NUM = 'VEZES_NUM'
TOKEN_TEMPO_VAL = 'TEMPO_VAL'
TOKEN_NAVEGAR_BROWSER = 'NAVEGAR_BROWSER'
TOKEN_VISUALIZAR_PDF_BROWSER = 'VISUALIZAR_PDF_BROWSER'
TOKEN_VISUALIZAR_VIDEO_BROWSER = 'VISUALIZAR_VIDEO_BROWSER'
TOKEN_VIDEOCONFERENCIA_BROWSER = 'VIDEOCONFERENCIA_BROWSER'
TOKEN_WHATSAPP_WEB_BROWSER = 'WHATSAPP_WEB_BROWSER'
TOKEN_EMAIL_BROWSER = 'EMAIL_BROWSER'
TOKEN_BROWSER_NAVEGADOR = 'BROWSER_NAVEGADOR'
TOKEN_EXECUTAR_CHROME = 'EXECUTAR_CHROME'
TOKEN_LINK = 'Link'

# Crie a tabela de tokens usando um dicionário
token_table = {
    'programa_SOL': TOKEN_PROGRAMA_SOL,
    'loop': TOKEN_LOOP,
    'vezes': TOKEN_VEZES,
    'sequência': TOKEN_SEQUENCIA,
    'Present': TOKEN_PRESENT,
    'tempo': TOKEN_TEMPO,
    'fases_EPIC': TOKEN_FASES_EPIC,
    'Explore': TOKEN_EXPLORE,
    'navegar': TOKEN_NAVEGAR,
    'visualizar_pdf': TOKEN_VISUALIZAR_PDF,
    'visualizar_vídeo': TOKEN_VISUALIZAR_VIDEO,
    'videoconferência': TOKEN_VIDEOCONFERENCIA,
    'Interact': TOKEN_INTERACT,
    'whatsapp_web': TOKEN_WHATSAPP_WEB,
    'email': TOKEN_EMAIL,
    'Critique': TOKEN_CRITIQUE,
    '1': TOKEN_VEZES_NUM,  # Números para vezes
    '2': TOKEN_VEZES_NUM,
    '3': TOKEN_VEZES_NUM,
    '4': TOKEN_VEZES_NUM,
    '5': TOKEN_VEZES_NUM,
    '20_min;': TOKEN_TEMPO_VAL,  # Valores de tempo
    '1_hora;': TOKEN_TEMPO_VAL,
    '1_dia;': TOKEN_TEMPO_VAL,
    '2_dias;': TOKEN_TEMPO_VAL,
    'sem_limite;': TOKEN_TEMPO_VAL,
    '15_min;': TOKEN_TEMPO_VAL,
    '10_seg;': TOKEN_TEMPO_VAL,
    'navegar': TOKEN_NAVEGAR_BROWSER,
    'browser': TOKEN_BROWSER_NAVEGADOR,
    'visualizar_pdf': TOKEN_VISUALIZAR_PDF_BROWSER,
    'link_pdf': TOKEN_LINK,
    'visualizar_vídeo': TOKEN_VISUALIZAR_VIDEO_BROWSER,
    'link_video': TOKEN_LINK,
    'videoconferência': TOKEN_VIDEOCONFERENCIA_BROWSER,
    'link_videoconferencia': TOKEN_LINK,
    'whatsapp_web': TOKEN_WHATSAPP_WEB_BROWSER,
    'link_whatsapp_web': TOKEN_LINK,
    'email': TOKEN_EMAIL_BROWSER,
    'link_email': TOKEN_LINK,
    'navegador': TOKEN_BROWSER_NAVEGADOR,
    'executar_o_Chrome_no_computador': TOKEN_EXECUTAR_CHROME
}
idx = 0
error_message = ''


def lexan(code):
    global token_list
    global error_message

    token_list = code.split(' ')

    for idx, palavra in enumerate(token_list, start=1):
        token_type = token_table.get(palavra, 'TOKEN_DESCONHECIDO')
        if token_type == 'TOKEN_DESCONHECIDO':
            error_message += f"'{palavra}' token invalido"
            return False
    return True


def whatsapp_wb():
    global idx
    flag = browser()
    if idx >= len(token_list):
        return False
    token = token_list[idx]
    idx += 1
    return flag and token == "link_whatsapp_web"


def videoconferencia():
    global idx
    flag = browser()
    if idx >= len(token_list):
        return False
    token = token_list[idx]
    idx += 1
    return flag and token == "link_videoconferencia"


def visualizar_video():
    global idx
    flag = browser()
    if idx >= len(token_list):
        return False
    token = token_list[idx]
    idx += 1
    return flag and token == "link_video"


def visualizar_pdf():
    global idx
    flag = browser()
    if idx >= len(token_list):
        return False
    token = token_list[idx]
    idx += 1
    return flag and token == "link_pdf"


def email():
    global idx
    flag = browser()
    if idx >= len(token_list):
        return False
    token = token_list[idx]
    idx += 1
    return flag and token == "link_email"


def browser():
    global idx
    if idx >= len(token_list):
        return False
    token = token_list[idx]
    idx += 1
    return token == "navegador"


def navegar():
    return browser()


def close_browser():
    import time
    import selenium.webdriver as webdriver
    tempo = token_list[idx - 1]
    driver = webdriver.Chrome()
    link = token_list[idx - 2]

    if (link == "link_videoconferencia"):
        link = "https://meet.google.com/"
    elif (link == "link_video"):
        link = "https://www.youtube.com/"
    elif (link == "link_pdf"):
        link = "https://drive.google.com/"
    elif (link == "link_whatsapp_web"):
        link = "https://web.whatsapp.com/"
    elif (link == "link_email"):
        link = "https://mail.google.com/"
    else:
        link = ""

    driver.get(link)
    
    if (tempo == "sem_limite;"):
        tempo = 999999999
        return True
    elif (tempo == "15_min;"):
        tempo = 60 * 15
    elif (tempo == "20_min;"):
        tempo = 60 * 20
    elif (tempo == "1_hora;"):
        tempo = 60 * 60
    elif (tempo == "1_dia;"):
        tempo = 60 * 60 * 24
    elif (tempo == "2_dias;"):
        tempo = 60 * 60 * 24 * 2
    elif (tempo == "10_seg;"):
        tempo = 10
    else:
        tempo = 999999999

    time.sleep(int(tempo))
    driver.close()
    return True


def tempo():
    global idx
    if idx >= len(token_list):
        return False
    token = token_list[idx]
    idx += 1
    return token_table[token] == TOKEN_TEMPO_VAL


def Explore():
    global idx
    if idx >= len(token_list):
        return False
    last_idx = idx
    if navegar() and tempo():
        return True
    idx = last_idx
    return False


def Present():
    global idx
    if idx >= len(token_list):
        return False
    last_idx = idx
    if visualizar_pdf() and tempo():
        return True
    idx = last_idx

    if visualizar_video() and tempo():
        return True
    idx = last_idx

    if videoconferencia() and tempo():
        return True
    idx = last_idx
    return False


def Interact():
    global idx
    if idx >= len(token_list):
        return False
    last_idx = idx
    if whatsapp_wb() and tempo():
        return True
    idx = last_idx

    if email() and tempo():
        return True
    idx = last_idx

    if videoconferencia() and tempo():
        return True
    idx = last_idx


def Critique():
    global idx
    if idx >= len(token_list):
        return False
    last_idx = idx
    if whatsapp_wb() and tempo():
        return True
    idx = last_idx

    if email() and tempo():
        return True
    idx = last_idx

    if videoconferencia() and tempo():
        return True
    idx = last_idx


def vezes():
    global idx
    if idx >= len(token_list):
        return False
    token = token_list[idx]
    idx += 1
    return token in {"1", "2", "3", "4", "5"}


def fases_EPIC():
    global idx
    if idx >= len(token_list):
        return False
    last_idx = idx
    if Explore():
        return True
    idx = last_idx

    if Present():
        return True
    idx = last_idx

    if Interact():
        return True
    idx = last_idx

    if Critique():
        return True

    return False


def sequencia():
    global idx
    last_idx = idx
    while fases_EPIC():
        if idx >= len(token_list):
            return True
    idx = last_idx
    return False


def programa_SOL():
    global idx
    if idx >= len(token_list):
        return False
    token = token_list[idx]
    idx += 1
    if token == "loop":
        return vezes() and sequencia()
    return False


def main(code, close):
    global error_message
    global idx
    error_message = ""
    idx = 0
    if (close == "TRUE"):
        return close_browser()
    if not lexan(code):
        return {'lexer': False, 'parser': False, 'error': error_message}
    elif programa_SOL():
        return {'lexer': True, 'parser': True}
    else:
        return {'lexer': True, 'parser': False}
