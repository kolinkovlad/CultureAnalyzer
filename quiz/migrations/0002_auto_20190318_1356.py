# Generated by Django 2.1.5 on 2019-03-18 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quizzes',
            options={'permissions': (('view_test_player', 'Can view the test player'),)},
        ),
    ]
