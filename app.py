from values import send_message, get_chats

from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome_page():
    return render_template('welcome-page.html')


@app.route('/merge_request', methods=['POST'])
def merge_request():
    data = request.get_json()
    print(data)
    text = f"tracking_front: {data['user']['name']}({data['user']['username']}) сделал реквест с бранча " \
           f"**{data['object_attributes']['source_branch']}** на бранч " \
           f"**{data['object_attributes']['target_branch']}**, Последний коммит: " \
           f"{data['object_attributes']['last_commit']['message']}"
    if data['object_attributes']['state'] == 'opened':
        send_message(text)

    return text


@app.route('/push_event', methods=['POST'])
def push_event():
    data = request.get_json()
    text = f"{data['user_name']}({data['user_username']}) сделал пуш в реп, Количество коммитов: " \
           f"{data['total_commits_count']}"
    if data['object_kind'] == 'push':
        send_message(text)

    return text


@app.route('/deployment_event', methods=['POST'])
def deployment_event():
    data = request.get_json()
    print(data)
    text = f"Деплой({data['commit_title']}) на стэнд **{data['environment']}** "
    if data['status'] == 'success':
        text += 'прошел'
        send_message(text)
    elif data['status'] == 'failed':
        text += 'упал'
        send_message(text)

    return text


@app.route('/get_updates', methods=['GET'])
def get_updates():
    return get_chats()


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
