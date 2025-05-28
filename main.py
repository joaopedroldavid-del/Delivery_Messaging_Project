from Services.EnvioMensagens import send_message
from Messages.RegionMessage import regiao_message
from Messages.ReviewMessage import review_message

def main():
    
    Região_links = regiao_message()

    for index, link in enumerate(Região_links):
        send_message(link, index)

    Review_links = review_message()
    
    for index, link in enumerate(Review_links):
        send_message(link, index)

main()