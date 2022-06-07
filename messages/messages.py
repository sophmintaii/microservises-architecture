from flask import Flask, request


app = Flask(__name__)


@app.route('/message', methods=['GET'])
def message():
    return 'message service:)'


if __name__ == "__main__":
    app.run()
