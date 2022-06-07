from flask import Flask, request


app = Flask(__name__)


messages = dict()


@app.route('/logging', methods=['POST', 'GET'])
def logging():
    if request.method == 'POST':
        uid = request.form['id']
        text = request.form['text']
        messages[uid] = text

        print(f'uid: {uid}:\n\tmessage:{text}')

        return ''

    if request.method == 'GET':
        return str(list(messages.values()))


if __name__ == '__main__':
    app.run()
