from django.contrib import admin
from chat_api.models import Message, TrendingTopics
# Register your models here.

admin.site.register([Message, TrendingTopics])
