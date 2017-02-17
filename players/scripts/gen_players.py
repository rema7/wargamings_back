import random
from optparse import OptionParser
import names
from players.models import Player


def reset(percent=50):
    return random.randrange(100) < percent


def generate_players():
    gender = 'male'
    if reset():
        gender = 'female'

    name = names.get_first_name(gender=gender)
    battles_total = random.randint(0, 200)
    wins_total = random.randint(0, battles_total)
    days_total = 123
    vehicles_x = random.randint(0, 25)
    if battles_total == 0:
        exp_total = 0
    else:
        exp_total = random.randint(1000, 100000)

    is_hidden = reset(20)

    player = Player(
        name=name,
        battles_total=battles_total,
        wins_total=wins_total,
        days_total=days_total,
        vehicles_x=vehicles_x,
        exp_total=exp_total,
        is_hidden=is_hidden
    )

    player.save()


def run():
    generate_players()

