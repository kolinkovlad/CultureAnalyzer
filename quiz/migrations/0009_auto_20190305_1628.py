# Generated by Django 2.1.5 on 2019-03-05 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20190214_1233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quizzes',
            options={'permissions': (('view_test_player', 'Can view the test player'),)},
        ),
    ]
