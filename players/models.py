from django.db import models
from django.template.defaultfilters import floatformat


class Player(models.Model):
    name = models.CharField(max_length=255, unique=True)
    battles_total = models.IntegerField(verbose_name='Total battles')
    wins_total = models.IntegerField(verbose_name='Total wins')
    days_total = models.IntegerField(verbose_name='Totals days in game')
    vehicles_x = models.IntegerField(verbose_name='Number of 10lvl vehicles')
    exp_total = models.BigIntegerField(verbose_name='Total experience')
    is_hidden = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # rating
    # exp_avg

    def rating(self):
        if self.wins_total == 0:
            return 0
        else:
            return floatformat(self.wins_total/self.days_total, 4)

    def exp_avg(self):
        if self.days_total == 0:
            return 0
        else:
            return floatformat(self.exp_total / self.days_total, 4)

    exp_avg.short_description = 'average experience'

    def __str__(self):
        return self.name

