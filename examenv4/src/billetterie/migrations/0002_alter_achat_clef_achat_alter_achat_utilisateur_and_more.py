# Generated by Django 5.0.4 on 2024-04-30 14:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billetterie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achat',
            name='clef_achat',
            field=models.CharField(blank=True, max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='achat',
            name='utilisateur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='clef_unique',
            field=models.CharField(default='eMyQrHE9ewL36j6R', max_length=16, unique=True),
        ),
    ]
