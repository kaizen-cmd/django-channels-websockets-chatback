from django.urls import path
from chat_api import consumers

websocket_urlpatterns = [
    path("", consumers.PublicChatConsumer.as_asgi())
]
