import requests
import uuid
from flask import Flask, request


app = Flask(__name__)


logging_client = "http://localhost:8081/logging"
messages_client = "http://localhost:8082/messages"


@app.route('/facade', methods=['POST', 'GET'])
def facade_service():
    if request.method == 'POST':
        message = {
            'id': uuid.uuid4(),
            'text': request.get_json()
        }

        res = requests.post(logging_client, message)

        return res.text

    if request.method == 'GET':
        res = f'{requests.get(logging_client).text} : {requests.get(messages_client).text}'


if __name__ == '__main__':
    app.run()
