# Generated by Django 3.1.7 on 2021-04-04 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spellbee', '0003_auto_20210404_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='pickword',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wordscore', to='spellbee.beeword', unique=True),
        ),
    ]
