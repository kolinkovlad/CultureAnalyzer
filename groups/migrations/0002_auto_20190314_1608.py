# Generated by Django 2.1.5 on 2019-03-14 16:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='mentor',
            field=models.ManyToManyField(related_name='mentor_in_group',
                                         to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='user',
            field=models.ManyToManyField(related_name='user_in_group',
                                         to=settings.AUTH_USER_MODEL),
        ),
    ]
