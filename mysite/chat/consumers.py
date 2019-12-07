# chat/consumers.py
from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync
#from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
from .models import Message
import json

User = get_user_model()

#class ChatConsumer(AsyncWebsocketConsumer):
class ChatConsumer(WebsocketConsumer):
    # Gets previous messages
    def fetch_messages(self, data):
        # Gets the last 15 created messages
        messages = Message.last_15_messages()
        content = {
            'messages':self.messages_to_json(messages)
        }
        # Send the chat message
        self.send_chat_message(content)

    # Returns a list of messages represented as JSON objects
    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    # Returns only ONE JSON object
    def message_to_json(self, message):
        return {
            'author':message.author.username,
            'content':message.content,
            'timestamp':str(message.timestamp)
        }

    # Sends a new message with the author
    def new_message(self, data):
        author = data['from']
        author_user = User.objects.filter(username=author)[0]
        message = Message.objects.create(
            author=author_user,
            content=data['message'])
        content = {
            'command':'new_message',
            'message':self.message_to_json(message)
        }
        return self.send_chat_message(content)

    commands = {
        'fetch_messages':fetch_messages,
        'new_message':new_message
    }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        # Grabs the command used
        self.commands[data['command']](self, data)

    # Send the message
    def send_chat_message(self, message):
        message = data['message']
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                #"username": self.scope["user"].username,
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    # Grabs the message from the event then sends it
    def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps(message))
