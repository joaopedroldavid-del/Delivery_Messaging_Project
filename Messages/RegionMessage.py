from Connection.ConnectionDB import cnxn
import pandas as pd 
import base64
import urllib.parse 

def regiao_message():
    with open("SQLs/Região.sql", "r", encoding="utf-8") as file:
        sql_query = file.read()

    data_frame = pd.read_sql(sql_query, cnxn) 

    data_frame["MESSAGE"] = ("Bom dia! Aqui é da equipe de entrega da xxxxxx!\n\n"+
                            "Para garantir a sua melhor experiência de entrega, por favor poderia confirmar alguns dados?\n\n"+
                            "Número do Pedido: *"+ data_frame["PEDIDO"].astype(int).astype(str) + "*\n"+
                            "Data de Entrega: *"+ data_frame["DTENTREGA"].dt.strftime("%d/%m/%Y") +"*\n"+
                            "Endereço da Entrega: *"+ data_frame["ENDERECO_ENTREGA"] +"*\n"+
                            "- Caso todos os dados estejam corretos, digite 'OK'\n\n"+
                            "- A data de entrega será essa mesmo? Se não, qual data de sua preferência?\n\n"+
                            "- O endereço de entrega está correto?\n\n"
                            "* Se houver alguma dificuldade de acesso ao endereço (rua estreita, escada...), pode nos informar?\n\n"
                            "Agradecemos sua colaboração, em breve o seu produto será entregue! Muito obrigado por escolher a xxxxxx para a realização de sua compra!")
    data_frame["LINK MESSAGE"] = "https://web.whatsapp.com/send" + "?" + "phone=55"+ data_frame["FONECEL"] + "&text=" + data_frame["MESSAGE"].apply(lambda x: urllib.parse.quote(x))

    links = data_frame["LINK MESSAGE"]

    return links