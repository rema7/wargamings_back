from rest_framework import serializers
from .models import Player

# rating
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'battles_total',
                  'wins_total', 'days_total', 'vehicles_x',
                  'exp_total',
                  'is_hidden',
                  'created_at')
