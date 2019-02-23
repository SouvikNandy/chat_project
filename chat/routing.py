from django.urls import re_path

from chat import sync_consumers, async_consumers

websocket_urlpatterns = [
    # re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', sync_consumers.ChatConsumer),
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', async_consumers.ChatConsumer),
]
