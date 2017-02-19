from rest_framework import generics

from .serializers import PlayerSerializer
from .models import Player


class PlayerList(generics.ListAPIView):
    model = Player
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

