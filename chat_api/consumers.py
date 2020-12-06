from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync


class PublicChatConsumer(WebsocketConsumer):

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            "abc",
            self.channel_name
        )
        self.accept()

    def disconnect(self):
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

    def chat_message(self, event):

        message = event["message"]
        name = event["name"]
        self.send(text_data=json.dumps(
            {"message": message, "name": name}))
