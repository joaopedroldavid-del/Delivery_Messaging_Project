from Connection.ConnectionDB import cnxn
import pandas as pd 
import base64
import urllib.parse 

def review_message():
    with open("SQLs/Avaliação.sql", "r", encoding="utf-8") as file:
        sql_query = file.read()

    data_frame = pd.read_sql(sql_query, cnxn)    

    data_frame["PEDIDO BASE64"] = data_frame["PEDIDO"].apply(lambda x: base64.b64encode(str(int(x)).encode()).decode())
    data_frame["LINK ASSESSMENT"] = "https://link.com.br" + data_frame["PEDIDO BASE64"]
    data_frame["MESSAGE"] = (
        "Prezado(a) Sr(a). *" + data_frame["NOME"] + "*,\n" +
        "Esperamos que esteja satisfeito com nosso serviço de entrega referente ao pedido: *" + data_frame["PEDIDO"].astype(int).astype(str) + "*. " +
        "Sua opinião é muito importante para nós e gostaríamos de convidá-lo(a) a compartilhar sua experiência.\n\n" +
        "Por favor, clique no link abaixo para avaliar nosso serviço. Sua avaliação nos ajudará a melhorar e oferecer um serviço cada vez melhor.\n\n" +
        data_frame["LINK ASSESSMENT"] + "\n\n" +
        "Agradecemos antecipadamente por sua contribuição!\n\n" +
        "Caso necessite de apoio, entre em contato pelo telefone: (DDD) 9999-9999")
    data_frame["LINK MESSAGE"] = "https://web.whatsapp.com/send" + "?" + "phone=55"+ data_frame["FONECEL"] + "&text=" + data_frame["MESSAGE"].apply(lambda x: urllib.parse.quote(x))

    links = data_frame["LINK MESSAGE"]
    
    return links