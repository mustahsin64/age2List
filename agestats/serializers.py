from dataclasses import fields
from rest_framework import serializers
from .models import Unit

class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = ['name','hp','attack','meele_armor','pierce_armor','range','speed','los','search_radius','creation_time','cost_wood','cost_food','cost_gold','cost_stone','attack_type']