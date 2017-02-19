import json

from django.db import IntegrityError
from django.test import TestCase

from django.utils import timezone

from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase

from players.models import Player


class PlayerTestCase(TestCase):
    def setUp(self):
        Player.objects.create(
            name="Player1",
            battles_total=10,
            wins_total=5,
            days_total=10,
            vehicles_x=2,
            exp_total=1000,
            is_hidden=False,
            created_at=timezone.now()
        )

    def test_unique_name(self):
        self.assertRaises(IntegrityError, Player.objects.create,
                          name="Player1",
                          battles_total=20,
                          wins_total=53,
                          days_total=102,
                          vehicles_x=21,
                          exp_total=10020,
                          is_hidden=False,
                          created_at=timezone.now())


class PlayersApiTestCase(APITestCase):
    def setUp(self):
        Player.objects.create(
            name="Player1",
            battles_total=10,
            wins_total=5,
            days_total=10,
            vehicles_x=2,
            exp_total=1000,
            is_hidden=False,
            created_at=timezone.now()
        )
        Player.objects.create(
            name="Player2",
            battles_total=6,
            wins_total=5,
            days_total=20,
            vehicles_x=12,
            exp_total=2000,
            is_hidden=False,
            created_at=timezone.now()
        )

    def test_get_players(self):
        response = self.client.get('/players')
        self.assertEqual(len(response.data), 2)
        resp = json.loads(response.content)
        self.assertEqual('Player1', resp[0]['name'])
        self.assertEqual('Player2', resp[1]['name'])
