from urllib import request, parse

bot_api = '1331155386:AAEKWdb-XdW0-4ykTRgel4byIIAZ1bO6kvI'


def send_message(text: str):
    parsed_text = parse.quote(text)
    req = request.Request(f'https://api.telegram.org/bot{bot_api}/sendMessage?chat_id=-1001132409362&text={parsed_text}')
    request.urlopen(req)
