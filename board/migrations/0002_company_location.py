# Generated by Django 3.2.5 on 2022-03-04 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]