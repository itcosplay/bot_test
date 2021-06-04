from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():

    return '<h1>Hello bot</h1>'


if __name__ == '__main__':
    app.run()


    
# https://api.telegram.org/bot1771447140:AAFeYJ_93P_cnakEg6nceNiD0Dh--k9bJqQ/setWebhook?url=https://44536005ab03.ngrok.io