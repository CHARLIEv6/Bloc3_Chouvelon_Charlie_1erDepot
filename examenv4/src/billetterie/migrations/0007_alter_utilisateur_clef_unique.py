# Generated by Django 5.0.4 on 2024-04-30 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billetterie', '0006_alter_utilisateur_clef_unique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='clef_unique',
            field=models.CharField(default='50BpR61v4gsycfcI', max_length=16, unique=True),
        ),
    ]
