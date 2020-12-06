from rest_framework.decorators import api_view
from rest_framework.response import Response
from chat_api.models import Message

@api_view(["GET"])
def get_logs(request):
    objs = Message.objects.all()
    msgs = [{"message": i.message, "name": i.name} for i in objs]
    return Response(msgs)