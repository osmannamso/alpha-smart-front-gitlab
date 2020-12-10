from urllib import request, parse

bot_api = '1331155386:AAEKWdb-XdW0-4ykTRgel4byIIAZ1bO6kvI'
dev_group_chat_id = '-351804047'
channel_chat_id = '-1001132409362'


def send_message(text: str):
    parsed_text = parse.quote(text)
    req = request.Request(f'https://api.telegram.org/bot{bot_api}/sendMessage?chat_id={channel_chat_id}&text={parsed_text}')
    request.urlopen(req)


def get_chats():
    req = request.Request(f'https://api.telegram.org/bot{bot_api}/getUpdates')
    resp = request.urlopen(req)
    print(resp.read())
