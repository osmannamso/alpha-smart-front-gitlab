from urllib import request, parse

bot_api = '1331155386:AAEKWdb-XdW0-4ykTRgel4byIIAZ1bO6kvI'


def send_message():
    text = parse.quote('Example From Bot')
    req = request.Request(f'https://api.telegram.org/bot{bot_api}/sendMessage?chat_id=-1001132409362&text={text}')
    request.urlopen(req)
