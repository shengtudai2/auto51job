# Generated by Django 4.0.1 on 2022-01-31 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='qq',
            field=models.CharField(default=None, max_length=20),
        ),
    ]