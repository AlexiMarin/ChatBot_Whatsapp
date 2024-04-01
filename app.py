from flask import Flask, request
import util as u
import whatsappservice as wss
import gptservices as gpt
import awsgi
import configparser

app = Flask(__name__)

@app.route('/welcome', methods=['GET'])
def index():
    return 'Welcome'

@app.route('/messaging', methods=['GET'])
def verify_token():
    try:
        accesstoken = '__token__'
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if token is not None and challenge is not None and token == accesstoken:
            return challenge
        else:
            return "", 400
    except:
        return "", 400

@app.route('/messaging', methods=['POST'])
def receive():
    try:
        body = request.json
        entry = body['entry'][0]
        changes = entry['changes'][0]
        value = changes['value']
        message = value['messages'][0]
        number = message['from']
        text = u.GetTextUser(message)

        print(f"{number} - {text}")

        #Integracion GPT
        responseGPT = gpt.GetResponse(text)
        if responseGPT != 'error':
            data = u.TextMessage(responseGPT, number)
            print(f"GPT        - {responseGPT}")
            wss.SendMessageWhatsapp(data)
        else:
            data = u.TextMessage("Lo siento", number)
            print(data)
            wss.SendMessageWhatsapp(data)

        return "EVENT_RECEIVED"
    except Exception as e:
        print("Error app processing the message:", e)
        return "EVENT_RECEIVED"

def lambda_handler(event, context):
    return awsgi.response(app, event, context)

if __name__ == "__main__":
    app.run()
