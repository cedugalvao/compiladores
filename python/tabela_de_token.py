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
token_list = "null"*40


def lexan(code):
    global token_list

    token_list = code.split()
    for idx, palavra in enumerate(token_list, start=1):
        token_type = token_table.get(palavra, 'TOKEN_DESCONHECIDO')
        if token_type == 'TOKEN_DESCONHECIDO':
            error_message = f"'{palavra}' token inválido"
            return {'lexer': False, 'parser': False, 'error': error_message}
    return {'lexer': True, 'parser': True}

def whatsapp_wb():
    global idx
    flag = browser()
    if idx >= len(token_list):
        return {'lexer': False, 'parser': False, 'error': "Fim inesperado do código"}
    token = token_list[idx]
    idx += 1
    return {'lexer': True, 'parser': flag and token == "link_whatsapp_web"}




def videoconferencia():
    global idx
    flag = browser()
    if idx >= len(token_list):
        return {'lexer': False, 'parser': False, 'error': "Fim inesperado do código"}
    token = token_list[idx]
    idx += 1
    return {'lexer': True, 'parser': flag and token == "link_videoconferencia"}


def visualizar_video():
    global idx
    flag = browser()
    if idx >= len(token_list):
        return {'lexer': False, 'parser': False, 'error': "Fim inesperado do código"}
    token = token_list[idx]
    idx += 1
    return {'lexer': True, 'parser': flag and token == "link_video"}


def visualizar_pdf():
    global idx
    flag = browser()
    if idx >= len(token_list):
        return {'lexer': False, 'parser': False, 'error': "Fim inesperado do código"}
    token = token_list[idx]
    idx += 1
    return {'lexer': True, 'parser': flag and token == "link_pdf"}


def email():
    global idx
    flag = browser()
    if idx >= len(token_list):
        return {'lexer': False, 'parser': False, 'error': "Fim inesperado do código"}
    token = token_list[idx]
    idx += 1
    return {'lexer': True, 'parser': flag and token == "link_email"}


def browser():
    global idx
    if idx >= len(token_list):
        return False
    token = token_list[idx]
    idx += 1
    print("bababbaa", token)
    return token == "navegador"


def navegar():
    return browser()


def tempo():
    global idx
    if idx >= len(token_list):
        return {'lexer': False, 'parser': False, 'error': "Fim inesperado do código"}
    token = token_list[idx]
    print(idx)
    idx += 1
    return {'lexer': True, 'parser': token_table.get(token) == TOKEN_TEMPO_VAL}


def Explore():
    global idx
    if idx >= len(token_list):
        return {'lexer': False, 'parser': False, 'error': "Fim inesperado do código"}
    last_idx = idx
    nav_result = navegar()
    temp_result = tempo()
    if nav_result['parser'] and temp_result['parser']:
        return {'lexer': nav_result['lexer'] and temp_result['lexer'], 'parser': True}
    idx = last_idx
    return {'lexer': nav_result['lexer'] and temp_result['lexer'], 'parser': False, 'error': 'Erro na análise de Explore'}



def Present():
    global idx
    if idx >= len(token_list):
        return {'lexer': False, 'parser': False, 'error': "Fim inesperado do código"}
    last_idx = idx
    pdf_result = visualizar_pdf()
    temp_result = tempo()
    if pdf_result['parser'] and temp_result['parser']:
        return {'lexer': pdf_result['lexer'] and temp_result['lexer'], 'parser': True}
    idx = last_idx

    video_result = visualizar_video()
    temp_result = tempo()
    if video_result['parser'] and temp_result['parser']:
        return {'lexer': video_result['lexer'] and temp_result['lexer'], 'parser': True}
    idx = last_idx

    videoconferencia_result = videoconferencia()
    temp_result = tempo()
    if videoconferencia_result['parser'] and temp_result['parser']:
        return {'lexer': videoconferencia_result['lexer'] and temp_result['lexer'], 'parser': True}
    idx = last_idx
    return {'lexer': False, 'parser': False, 'error': 'Erro na análise de Present'}


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
    print(idx, token_list)
    if idx >= len(token_list):
        return False
    token = token_list[idx]
    idx += 1
    return token in {"1", "2", "3", "4", "5"}


def fases_EPIC():
    global idx
    if idx >= len(token_list):
        return False
    print(idx)
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
    if fases_EPIC():
        print("a")
        return True
    idx = last_idx
    if fases_EPIC() and sequencia():
        return True

    return False


def programa_SOL(code):
    global idx
    global error_message
    error_message = ""
    idx = 0
    if idx >= len(token_list):
        return {'lexer': False, 'parser': False, 'error': "Fim inesperado do código"}
    token = token_list[idx]
    idx += 1
    if token == "loop":
        result = vezes()
        if result['parser']:
            result_seq = sequencia()
            return {'parser': result_seq['parser'], 'error': result_seq['error']} if not result['lexer'] else result_seq
        else:
            return result
    else:
        return {'lexer': False, 'parser': False, 'error': f"Token inesperado na posição {idx}: '{token}'"}



def main(code):
    global idx
    idx = 0
    if not lexan(code):
        print("Nao difernet")
        return lexan(code)
    elif programa_SOL():
        print("SIM")
        return "lexer e parser okPASSOU"
    else:
        print("NO")
        return "NÂO"