import requests
import time
import json
import os

class telegramBot:
    def __init__(self):
        token = '1629560365:AAHRiUJcVnR3dZqRbRYqzuGC9xBwWst2F8k'
        self.url_base = f'https://api.telegram.org/bot{token}/'
        
    #iniciar o bot
    def iniciar_bot(self):
        update_id = None
        while True:
            atualizacao = self.obter_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado['message']['from']['id']
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)
    #obter mensagens
    def obter_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)    
        return json.loads(resultado.content)

    #criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        if eh_primeira_mensagem == True:
            return f'''Olá, Boa Noite! Eu sou o Sr. Robô, seu assistente virtual de compras online. Digite a opção do assunto que deseja tratar.{os.linesep}1 - Problema com a entrega{os.linesep}2 - Devolução{os.linesep}3 - Solicitar reembolso{os.linesep}4 - Tirar dúvidas{os.linesep} 5 - Efetuar nova compra{os.linesep}6 - Troca de produto'''
        if mensagem == "1":
            return f'''Desde já lamento por ter sofrido problemas na entrega, fazemos de tudo para efetuar o envio correto do produto dentro do prazo estabelecido. Por favor, digite o número do pedido para que eu possa verificar'''

    #responder
    def responder(self, resposta, chat_id):
        #enviar
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)



bot = telegramBot()
bot.iniciar_bot()



