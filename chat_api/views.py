from rest_framework.generics import ListAPIView
from chat_api.models import Message, TrendingTopics
from chat_api.serilaizers import MessageSerilaizer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response


class ChatLogsView(ListAPIView):
    queryset = Message.objects.all().order_by("-timestamp")
    serializer_class = MessageSerilaizer
    pagination_class = PageNumberPagination


class TopicsView(APIView):

    def get(self, request):
        queryset = TrendingTopics.objects.all()
        serialized_topics = [topic.topic for topic in queryset]
        return Response(serialized_topics)
