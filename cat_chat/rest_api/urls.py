from cat.consumers import ChatConsumer
from django.urls import include, path
from rest_framework import routers

from rest_api.views import CatViewSet, RegisterViev

router = routers.SimpleRouter()
router.register(r'cats', CatViewSet, basename='cat')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls')),
    path('register/', RegisterViev.as_view()),
    path('ws/chat/<int:user_id>/', ChatConsumer.as_asgi()),
]
