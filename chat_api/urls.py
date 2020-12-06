from django.urls import path
from chat_api import views

urlpatterns = [
    path("logs/", views.get_logs)
]
