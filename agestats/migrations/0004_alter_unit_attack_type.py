# Generated by Django 4.1.1 on 2022-10-13 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agestats', '0003_unit_attack_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='attack_type',
            field=models.CharField(choices=[('Meele', 'meele'), ('Pierce', 'Pierce')], default='Meele', max_length=50),
        ),
    ]
