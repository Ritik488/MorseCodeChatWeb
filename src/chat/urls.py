from django.urls import path, re_path
from .views import index, room, login, signup, ro


app_name = 'chat'

urlpatterns = [
    path('', login, name='login'),
    path('signup/', signup, name='signup'),
    path('roaming/', ro, name='ro'),
    path('index/', index, name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
]
