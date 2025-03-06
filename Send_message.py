import pyodbc
import pandas as pd 
import base64
import urllib.parse 
import pyautogui
import pyperclip
import webbrowser as web
import time
import os
import subprocess
import schedule as shd

cnxn = pyodbc.connect(
    'DRIVER={Oracle em OraClient19Home1};'
    'UID=USERNAME;'
    'PWD=PASSWORD;'
    'DBQ=SERVICE_NAME'
)

def limpeza_de_dados():
    pyautogui.hotkey('win', 'r')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.write('del /s /q %temp%\\*')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.write('cleanmgr /sagerun:1')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.write('exit')
    time.sleep(1)
    pyautogui.press('enter')

def abrir_excel_atrasos_BI():
    arquivo_excel = r"ADD THE FILE PATH"
    subprocess.Popen([r"ADD THE PROGRAM PATH", arquivo_excel])

def send_message(link, index):

    if (index % 2 != 0):
        web.get(r"ADD THE PROGRAM PATH").open(link)
    else: 
        web.get(r"ADD THE PROGRAM PATH").open(link)

    if(index <= 1):
        time.sleep(70) # First WhatsApp Open
    else:
        time.sleep(2)

    pyautogui.press('f11')
    time.sleep(25) 

    pyautogui.moveTo(800, 700, duration=0.1)
    time.sleep(0.05)

    pyautogui.click()

    pyautogui.press('enter')
    time.sleep(3)

    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)

    pyautogui.press('enter')

def review_message():
    with open("SQLs/Avaliação.sql", "r", encoding="utf-8") as file:
        sql_query = file.read()

    data_frame = pd.read_sql(sql_query, cnxn)    

    data_frame["PEDIDO BASE64"] = data_frame["PEDIDO"].apply(lambda x: base64.b64encode(str(int(x)).encode()).decode())
    data_frame["LINK ASSESSMENT"] = "https://av.XXXXX.com.br/av/avaliacao/index.xhtml?pedido=" + data_frame["PEDIDO BASE64"]
    data_frame["MESSAGE"] = (
        "Prezado(a) Sr(a). *" + data_frame["NOME"] + "*,\n" +
        "Esperamos que esteja satisfeito com nosso serviço de entrega referente ao pedido: *" + data_frame["PEDIDO"].astype(int).astype(str) + "*. " +
        "Sua opinião é muito importante para nós e gostaríamos de convidá-lo(a) a compartilhar sua experiência.\n\n" +
        "Por favor, clique no link abaixo para avaliar nosso serviço. Sua avaliação nos ajudará a melhorar e oferecer um serviço cada vez melhor.\n\n" +
        data_frame["LINK ASSESSMENT"] + "\n\n" +
        "Agradecemos antecipadamente por sua contribuição!\n\n" +
        "Caso necessite de apoio, entre em contato pelo telefone: (48) 4007-2022")
    data_frame["LINK MESSAGE"] = "https://web.whatsapp.com/send" + "?" + "phone=55"+ data_frame["FONECEL"] + "&text=" + data_frame["MESSAGE"].apply(lambda x: urllib.parse.quote(x))

    links = data_frame["LINK MESSAGE"]
    
    return links

def viagem_message():
    with open("SQLs/Viagem.sql", "r", encoding="utf-8") as file:
        sql_query = file.read()

    data_frame = pd.read_sql(sql_query, cnxn) 

    data_frame["MESSAGE"] = ("Bom dia! Aqui é da equipe de entrega da XXXXXX!\n\n"+
                            "Para garantir a sua melhor experiência de entrega, por favor poderia confirmar alguns dados?\n\n"+
                            "Número do Pedido: *"+ data_frame["PEDIDO"].astype(int).astype(str) + "*\n"+
                            "Data de Entrega: *"+ data_frame["DTENTREGA"].dt.strftime("%d/%m/%Y") +"*\n"+
                            "Endereço da Entrega: *"+ data_frame["ENDERECO_ENTREGA"] +"*\n"+
                            "- Caso todos os dados estejam corretos, digite 'OK'\n\n"+
                            "- A data de entrega será essa mesmo? Se não, qual data de sua preferência?\n\n"+
                            "- O endereço de entrega está correto?\n\n"
                            "* Se houver alguma dificuldade de acesso ao endereço (rua estreita, escada...), pode nos informar?\n\n"
                            "Agradecemos sua colaboração, em breve o seu produto será entregue! Muito obrigado por escolher a Cassol para a realização de sua compra!")
    data_frame["LINK MESSAGE"] = "https://web.whatsapp.com/send" + "?" + "phone=55"+ data_frame["FONECEL"] + "&text=" + data_frame["MESSAGE"].apply(lambda x: urllib.parse.quote(x))

    links = data_frame["LINK MESSAGE"]

    return links

def regiao_message():
    with open("SQLs/Região.sql", "r", encoding="utf-8") as file:
        sql_query = file.read()

    data_frame = pd.read_sql(sql_query, cnxn) 

    data_frame["MESSAGE"] = ("Bom dia! Aqui é da equipe de entrega da XXXXXX!\n\n"+
                            "Para garantir a sua melhor experiência de entrega, por favor poderia confirmar alguns dados?\n\n"+
                            "Número do Pedido: *"+ data_frame["PEDIDO"].astype(int).astype(str) + "*\n"+
                            "Data de Entrega: *"+ data_frame["DTENTREGA"].dt.strftime("%d/%m/%Y") +"*\n"+
                            "Endereço da Entrega: *"+ data_frame["ENDERECO_ENTREGA"] +"*\n"+
                            "- Caso todos os dados estejam corretos, digite 'OK'\n\n"+
                            "- A data de entrega será essa mesmo? Se não, qual data de sua preferência?\n\n"+
                            "- O endereço de entrega está correto?\n\n"
                            "* Se houver alguma dificuldade de acesso ao endereço (rua estreita, escada...), pode nos informar?\n\n"
                            "Agradecemos sua colaboração, em breve o seu produto será entregue! Muito obrigado por escolher a Cassol para a realização de sua compra!")
    data_frame["LINK MESSAGE"] = "https://web.whatsapp.com/send" + "?" + "phone=55"+ data_frame["FONECEL"] + "&text=" + data_frame["MESSAGE"].apply(lambda x: urllib.parse.quote(x))

    links = data_frame["LINK MESSAGE"]

    return links

def rio_grande_do_sul_message():
    with open("SQLs/RioGrandedoSul.sql", "r", encoding="utf-8") as file:
        sql_query = file.read()

    data_frame = pd.read_sql(sql_query, cnxn) 

    data_frame["MESSAGE"] = ("Olá, Sr/Srª "+ data_frame["NOME"] +". A *XXXXXX* agradece a sua compra! Seu pedido: *"+ data_frame["PEDIDO"].astype(int).astype(str) +"*, está previsto para entrega no dia *"+ data_frame["DTENTREGA"].dt.strftime("%d/%m/%Y") +", no seguinte endereço: *"+ data_frame["ENDERECO_ENTREGA"] +"* . \n\n"
                            "Responda:\n\n"
                            "1 - Para confirmar a entrega e o endereço.\n"
                            "2 - Caso o endereço de entrega possua algum grau de dificuldade de acesso.\n"
                            "3 - Caso necessite realizar alguma alteração na data de entrega ou endereço.\n\n"
                            "Para maiores informações sobre esta entrega envie mensagem para *(51) 99529-2832.*\n\n"
                            "Para apoio em demais assuntos, entrar em contato com *SAC* através dos números: *40011515 (whatsapp)* ou *40072022 (ligação).*")
    data_frame["LINK MESSAGE"] = "https://web.whatsapp.com/send" + "?" + "phone=55"+ data_frame["FONECEL"] + "&text=" + data_frame["MESSAGE"].apply(lambda x: urllib.parse.quote(x))

    links = data_frame["LINK MESSAGE"]

    return links

def parana_message():
    with open("SQLs/Parana.sql", "r", encoding="utf-8") as file:
        sql_query = file.read()

    data_frame = pd.read_sql(sql_query, cnxn) 

    data_frame["MESSAGE"] = ("Bom dia! Aqui é da equipe de entrega da XXXXXX!\n\n"+
                            "Para garantir a sua melhor experiência de entrega, por favor poderia confirmar alguns dados?\n\n"+
                            "Número do Pedido: *"+ data_frame["PEDIDO"].astype(int).astype(str) + "*\n"+
                            "Data de Entrega: *"+ data_frame["DTENTREGA"].dt.strftime("%d/%m/%Y") +"*\n"+
                            "Endereço da Entrega: *"+ data_frame["ENDERECO_ENTREGA"] +"*\n"+
                            "- Caso todos os dados estejam corretos, digite 'OK'\n\n"+
                            "- A data de entrega será essa mesmo? Se não, qual data de sua preferência?\n\n"+
                            "- O endereço de entrega está correto?\n\n"
                            "* Se houver alguma dificuldade de acesso ao endereço (rua estreita, escada...), pode nos informar?\n\n"
                            "Agradecemos sua colaboração, em breve o seu produto será entregue! Muito obrigado por escolher a Cassol para a realização de sua compra!")
    data_frame["LINK MESSAGE"] = "https://web.whatsapp.com/send" + "?" + "phone=55"+ data_frame["FONECEL"] + "&text=" + data_frame["MESSAGE"].apply(lambda x: urllib.parse.quote(x))

    links = data_frame["LINK MESSAGE"]

    return links

def main():
    
    Review_links = review_message()
    
    for index, link in enumerate(Review_links):
        send_message(link, index)

    Viagem_links = viagem_message()

    for index, link in enumerate(Viagem_links):
        send_message(link, index)

    Região_links = regiao_message()

    for index, link in enumerate(Região_links):
        send_message(link, index)

    RS_links = rio_grande_do_sul_message()

    for index, link in enumerate(RS_links):
        send_message(link, index)

    PR_links = parana_message()

    for index, link in enumerate(PR_links):
        send_message(link, index)

# Data Cleaning:
shd.every().monday.at("06:30").do(limpeza_de_dados)
shd.every().tuesday.at("06:30").do(limpeza_de_dados)
shd.every().wednesday.at("06:30").do(limpeza_de_dados)
shd.every().thursday.at("06:30").do(limpeza_de_dados)
shd.every().friday.at("06:30").do(limpeza_de_dados)
shd.every().saturday.at("06:30").do(limpeza_de_dados)

# delayed order:
shd.every().monday.at("07:10").do(abrir_excel_atrasos_BI)
shd.every().tuesday.at("07:10").do(abrir_excel_atrasos_BI)
shd.every().wednesday.at("07:10").do(abrir_excel_atrasos_BI)
shd.every().thursday.at("07:10").do(abrir_excel_atrasos_BI)
shd.every().friday.at("07:10").do(abrir_excel_atrasos_BI)
shd.every().saturday.at("07:10").do(abrir_excel_atrasos_BI)

# Message:
shd.every().monday.at("08:00").do(main)
shd.every().tuesday.at("08:00").do(main)
shd.every().wednesday.at("08:00").do(main)
shd.every().thursday.at("08:00").do(main)
shd.every().friday.at("08:00").do(main)
#shd.every().saturday.at("08:00").do(main)

cnxn.close()

while True:
    shd.run_pending()
    pyautogui.press('numlock')
    time.sleep(0.5)