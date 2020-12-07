from rest_framework.serializers import ModelSerializer
from chat_api.models import Message

class MessageSerilaizer(ModelSerializer):

    class Meta:

        model = Message
        fields = "__all__"