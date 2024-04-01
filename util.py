def GetTextUser(message):
    text = ""
    typeMessage = message['type']

    if typeMessage == 'text':
        text = message['text']['body'] 
    elif typeMessage == 'interactive':
        interactiveObject = message['interactive']
        typeInteractive = interactiveObject['type']
        if typeInteractive == 'button_reply':
            text = interactiveObject['button_reply']['title']
        elif typeInteractive == 'list_reply':
            text = interactiveObject['list_reply']['title']
        else:
            print('Sin Mensaje')
    else:
        print('Sin Mensaje')
    return text

def TextMessage(text, number):
    data = {
            'messaging_product': 'whatsapp',
            'to': number,
            'text': {
                'body': text
            },
            'type': 'text'
            }      
    return data

def TextFormatMessage(number):
    data = {
            'messaging_product': 'whatsapp',
            'to': number,
            'text': {
                'body': '\n_text'
            },
            'type': 'text'
            }      
    return data

def ImageMessage(number):
    data = {
            'messaging_product': 'whatsapp',
            'to': number,
            'image': {
                'link': 'https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/02/20/17084411767438.jpg'
            },
            'type': 'image'
            }      
    return data

# def AudioMessage(number):
#     data = {
#             'messaging_product': 'whatsapp',
#             'to': number,
#             'audio': {
#                 'link': 'https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/02/20/17084411767438.jpg'
#             },
#             'type': 'audio'
#             }      
#     return data

def DocumentMessage(number):
    data = {
            'messaging_product': 'whatsapp',
            'to': number,
            'document': {
                'link': 'C:\\Users\\alexi\\Downloads\\Reporte_RSI (1).pdf'
            },
            'type': 'document'
            }      
    return data

def VideotMessage(number):
    data = {
            'messaging_product': 'whatsapp',
            'to': number,
            'video': {
                'link': 'C:\\Users\\alexi\\Downloads\\Untitled video - Made with Clipchamp (1).mp4'
            },
            'type': 'video'
            }      
    return data

def LocationMessage(number):
    data = {
            'messaging_product': 'whatsapp',
            'to': number,
            'location': {
                'latitude': '',
                'longitude': '',
                'name': '',
                'address': ''
            },
            'type': 'location'
            }      
    return data

def ButtosnMessage(number):
    data = {
            'messaging_product': 'whatsapp',
            'to': number,
            'interactive': {
                'type': 'button',
                'body': {
                    'text': 'Probando_1'
                },
                'action': {
                    'buttons': [
                        {
                            'type': 'reply',
                            'reply': {
                                'id': '001',
                                'title': 'Sign up'
                            }
                        },
                        {
                            'type': 'reply',
                            'reply': {
                                'id': '002',
                                'title': 'Log in'
                            }
                        }
                    ]
                }
            },
            'type': 'interactive'
        }      
    return data

def ListMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "to": "51943662964",
            "type": "interactive",
            "interactive": {
                "type": "list",
                "body": {
                    "text": "✅ I have these options"
                },
                "footer": {
                    "text": "Select an option"
                },
                "action": {
                    "button": "See options",
                    "sections": [
                        {
                            "title": "Buy and sell products",
                            "rows": [
                                {
                                    "id": "main-buy",
                                    "title": "Buy",
                                    "description": "Buy the best product your home"
                                },
                                {
                                    "id": "main-sell",
                                    "title": "Sell",
                                    "description": "Sell your products"
                                }
                            ]
                        },
                        {
                            "title": "📍center of attention",
                            "rows": [
                                {
                                    "id": "main-agency",
                                    "title": "Agency",
                                    "description": "Your can visit our agency"
                                },
                                {
                                    "id": "main-contact",
                                    "title": "Contact center",
                                    "description": "One of our agents will assist you"
                                }
                            ]
                        }
                    ]
                }
            }
        }   
    return data


