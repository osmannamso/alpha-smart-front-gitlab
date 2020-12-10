from values import send_message

from flask import Flask
app = Flask(__name__)


@app.route('/merge_request', methods=['GET', 'POST'])
def merge_request():
    send_message()
    return 'Hello World!'


if __name__ == '__main__':
    app.run(threaded=True, port=5000)

app = Flask(__name__)
