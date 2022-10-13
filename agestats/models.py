from email.policy import default
from random import choices
from django.db import models

# Create your models here.

ATTACK_TYPE_CHOICES = [
    ('Meele', 'Meele'),
    ('Pierce', 'Pierce'),
]

class Unit(models.Model):
    name = models.CharField(max_length=200)
    hp = models.IntegerField()
    attack = models.IntegerField(default=0)
    meele_armor = models.IntegerField(default=0)
    pierce_armor = models.IntegerField(default=0)
    range = models.IntegerField(default=0)
    speed = models.FloatField(default=0.1)
    los = models.IntegerField(default=2)
    search_radius = models.IntegerField(default=2)
    creation_time = models.IntegerField(default=25)
    cost_wood = models.IntegerField(default=0)
    cost_food = models.IntegerField(default=0)
    cost_gold = models.IntegerField(default=0)
    cost_stone = models.IntegerField(default=0)
    attack_type = models.CharField(max_length=20,default='meele')
    attack_type = models.CharField(
        max_length=50, choices = ATTACK_TYPE_CHOICES, default = 'Meele'
    )

    def __str__(self):
        return self.name
