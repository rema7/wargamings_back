from django.conf.urls import url

from players.api import PlayerList

urlpatterns = [
    url(r'^players', PlayerList.as_view(), name='player-list'),
]
