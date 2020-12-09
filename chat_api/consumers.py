from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from chat_api.models import Message, TrendingTopics

counter = 0
online_users = {}


class PublicChatConsumer(WebsocketConsumer):

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            "abc",
            self.channel_name
        )
        global counter
        counter += 1
        self.accept()
        context = {
            "type": "online_count",
            "counter": counter,
            "online": list(online_users.values())
        }
        async_to_sync(self.channel_layer.group_send)("abc", context)

    def disconnect(self, close_code):
        global counter
        global online_users
        counter -= 1
        try:
            name = online_users[self.scope["client"][1]]
            del online_users[self.scope["client"][1]]
        except:
            name = None
        context = {
            "type": "online_count_1",
            "counter": counter,
            "online": list(online_users.values()),
            "name": name
        }
        async_to_sync(self.channel_layer.group_send)("abc", context)
        async_to_sync(self.channel_layer.group_discard)(
            "abc", self.channel_name)


    def receive(self, text_data):
        global online_users
        data = json.loads(text_data)
        message = data["message"]
        name = data["name"]
        context = {
            "type": "chat_message",
            "message": message,
            "name": name
        }
        async_to_sync(self.channel_layer.group_send)("abc", context)
        if message == "100pnotify":
            online_users[self.scope["client"][1]] = name
        else:
            Message.objects.create(name, message=message)

    def chat_message(self, event):

        message = event["message"]
        name = event["name"]
        self.send(text_data=json.dumps(
            {"message": message, "name": name}))

    def online_count(self, event):

        count = event["counter"]
        online = event["online"]
        self.send(text_data=json.dumps({"counter": count, "online": online}))

    def online_count_1(self, event):

        count = event["counter"]
        online = event["online"]
        name = event["name"]
        print(">>", online_users)
        self.send(text_data=json.dumps({"counter": count, "online": online, "disconnect": True, "name": name}))

