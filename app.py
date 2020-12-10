from values import send_message, get_chats

from flask import Flask, request
app = Flask(__name__)


@app.route('/merge_request', methods=['POST'])
def merge_request():
    data = request.get_json()
    print(data)
    text = f"tracking_front: {data['user']['name']}({data['user']['username']}) сделал реквест на бранч {data['object_attributes']['target_branch']}" \
           f", Последний коммит: {data['object_attributes']['last_commit']['message']}"
    if data['object_attributes']['state'] == 'opened':
        send_message(text)

    return text


@app.route('/get_updates', methods=['GET'])
def get_updates():
    data = request.get_data()
    get_chats()
    print(data)

    return 'asd'


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
