from rest_framework.generics import ListAPIView
from chat_api.models import Message
from chat_api.serilaizers import MessageSerilaizer
from rest_framework.pagination import PageNumberPagination


class ChatLogsView(ListAPIView):
    queryset = Message.objects.all().order_by("-timestamp")
    serializer_class = MessageSerilaizer
    pagination_class = PageNumberPagination


