from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from chat_api.models import Message


class PublicChatConsumer(WebsocketConsumer):

    counter = 0

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            "abc",
            self.channel_name
        )
        self.counter += 1
        self.accept()
        self.send(json.dumps({"count": self.counter}))

    def disconnect(self, close_code):
        self.counter += 1
        async_to_sync(self.channel_layer.group_discard)(
            "abc", self.channel_name)

    def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        name = data["name"]
        context = {
            "type": "chat_message",
            "message": message,
            "name": name
        }
        async_to_sync(self.channel_layer.group_send)("abc", context)
        Message.objects.create(name=name, message=message)

    def chat_message(self, event):

        message = event["message"]
        name = event["name"]
        self.send(text_data=json.dumps(
            {"message": message, "name": name}))
