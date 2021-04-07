from urllib import request, parse
import json

bot_api = '1331155386:AAHY05yymhyjoRWPTepZUwe4r0hdmwTv9Gw'
dev_group_chat_id = '-351804047'
channel_chat_id = '-1001132409362'
osman_chat_id = '300216268'

CURRENT_CHAT_ID = osman_chat_id


def send_message(text: str):
    parsed_text = parse.quote(text)
    req = request.Request(
        f'https://api.telegram.org/bot{bot_api}/sendMessage?chat_id={CURRENT_CHAT_ID}&text={parsed_text}')
    request.urlopen(req)


def get_chats():
    req = request.Request(f'https://api.telegram.org/bot{bot_api}/getUpdates')
    resp = request.urlopen(req)

    return json.loads(resp.read())
