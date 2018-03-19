# Generated by Django 2.0.2 on 2018-03-18 23:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180318_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupentity',
            name='managers',
            field=models.ManyToManyField(blank=True, help_text='Users who can accept/decline requests.', null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
