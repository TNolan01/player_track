# Generated by Django 3.2.13 on 2022-06-06 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20220605_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_selection',
            name='jersey_number',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25')], null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='team_selection',
            name='player',
            field=models.ManyToManyField(to='tracker.Player'),
        ),
    ]
