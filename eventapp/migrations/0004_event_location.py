# Generated by Django 2.2.28 on 2024-04-24 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0003_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='Campus Center', max_length=100),
            preserve_default=False,
        ),
    ]