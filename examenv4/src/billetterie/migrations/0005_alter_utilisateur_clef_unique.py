# Generated by Django 5.0.4 on 2024-04-30 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billetterie', '0004_alter_utilisateur_clef_unique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='clef_unique',
            field=models.CharField(default='8UE8G0hmcRdBlIZD', max_length=16, unique=True),
        ),
    ]
