# Generated by Django 4.0.6 on 2022-07-09 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0019_alter_orders_saler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salerdetail',
            name='gst_Number',
            field=models.IntegerField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='salerdetail',
            name='state',
            field=models.CharField(choices=[('Montserrado', 'Montserrado'), ('Margibi', 'Margibi'), ('Maryland', 'Maryland'), ('Grandkru', 'Grandkru'), ('Grandgedeh', 'Grandgedeh'), ('Sinoe', 'Sinoe'), ('Bomi', 'Bomi'), ('Grandcapemount', 'Grandcapemounnt'), ('Gbarpolu', 'Gbarpolu'), ('Rivercess', 'Rivercess'), ('Grand Bassa', 'Grand Bassa'), ('Nimba', 'Nimba')], max_length=50, null=True),
        ),
    ]
