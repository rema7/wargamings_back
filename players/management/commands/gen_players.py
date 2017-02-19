from datetime import datetime, timedelta
from django.utils import timezone
import random
import names
from django.core.management import BaseCommand
from django.db import IntegrityError

from players.models import Player


class Command(BaseCommand):
    help = 'Generate players data'

    def reset(self, percent=50):
        return random.randrange(100) < percent

    def add_arguments(self, parser):
        parser.add_argument('--number',
                            dest='number',
                            default=10,
                            type=int,
                            help='generate new players')

    def handle(self, *args, **options):
        number = 10

        if options['number']:
            number = options['number']

        for i in range(0, number):
            gender = 'male'

            if self.reset():
                gender = 'female'

            name = names.get_first_name(gender=gender)
            battles_total = random.randint(0, 1200)
            wins_total = random.randint(0, battles_total)

            if wins_total > 0:
                days_total = random.randint(1, 1000)
            else:
                days_total = 0

            vehicles_x = random.randint(0, 25)
            if battles_total == 0:
                exp_total = 0
            else:
                exp_total = random.randint(1000, 100000)

            is_hidden = self.reset(15)

            date = timezone.now() - timedelta(days=days_total)

            player = Player(
                name=name,
                battles_total=battles_total,
                wins_total=wins_total,
                days_total=days_total,
                vehicles_x=vehicles_x,
                exp_total=exp_total,
                is_hidden=is_hidden,
                created_at=date
            )

            try:
                player.save()
            except IntegrityError as e:
                print('Catch unique name')
                player.name += str(random.randint(1, 9999))
                player.save()


