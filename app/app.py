import json
import os

from app.gorgeous import Gorgeous
from flask import Flask, abort, render_template, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

token = os.environ.get('CHANNEL_ACCESS_TOKEN')
secret = os.environ.get('CHANNEL_SECRET')

assert token is not None and secret is not None,\
    "CHANNEL_ACCESS_TOKEN or CHANNEL_SECRET is not set correctly"

line_bot_api = LineBotApi(token)
handler = WebhookHandler(secret)

g = Gorgeous()

# for Web App
@app.route('/', methods=['POST', 'GET'])
def home():
    html = render_template('index.html')
    if request.method == 'POST':
        html = render_template('index.html',
            result=g.revolution(request.form["input"]))
    return html


# for LINE bot
@app.route("/callback", methods=['POST', 'GET'])
def callback():
    if request.method == 'GET':
        return g.revolution("まだ助かる")

    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    ans = g.revolution(event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=ans))


@app.route("/test", methods=['POST', 'GET'])
def run_test():
    t = "まだ助かる"
    if request.method == "POST":
        t = request.get_data(as_text=True)
    return g.revolution(t)


if __name__ == "__main__":
    app.run()
