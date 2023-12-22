import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps
                  ({'message': 'connection_established',
                    'data': "You're connected to the server",
                    'status':200
                    }))
        
    def recieve(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)
        # self.send(text_data=json.dumps
        #           ({'message': 'message_recieved',
        #             'data': message,
        #             'status':200
        #             }))

    