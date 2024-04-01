from openai import OpenAI
import configparser
config = configparser.ConfigParser()
config.read('credentials.txt')
gpt = config['gpt']
token = gpt['token']
client = OpenAI(api_key = token)

def GetResponse(text):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."}, 
                      {"role": "user", "content": text}],
        )
        response_message = response.choices[0].message.content
        return response_message
    except Exception as e:
        return "error gpt"