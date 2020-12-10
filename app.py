from values import send_message

from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/merge_request', methods=['POST'])
def merge_request():
    data = request.get_json()
    text = f"{data['user']['name']} под username {data['user']['username']} сделал реквест на бранч {data['merge_request']['source']['default_branch']}"
    send_message(text)
    return text


if __name__ == '__main__':
    app.run(threaded=True, port=6001)
