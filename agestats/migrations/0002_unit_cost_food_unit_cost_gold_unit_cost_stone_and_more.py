# Generated by Django 4.1.1 on 2022-10-13 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agestats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='cost_food',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='unit',
            name='cost_gold',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='unit',
            name='cost_stone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='unit',
            name='cost_wood',
            field=models.IntegerField(default=0),
        ),
    ]
