from cat.models import Cat
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from rest_api.serializers import CatSerializer, RegisterSerializer


class CatViewSet(viewsets.ModelViewSet):
    serializer_class = CatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cat.objects.filter(user=self.request.user)


class RegisterViev(generics.CreateAPIView):
    serializer_class = RegisterSerializer
