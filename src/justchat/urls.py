from django.contrib import admin
from django.urls import path, include
from chat.views import login

urlpatterns = [
    path('', login, name='login'),
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls', namespace='chat')),
]
