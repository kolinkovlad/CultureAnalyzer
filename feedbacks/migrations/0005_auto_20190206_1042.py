# Generated by Django 2.1.5 on 2019-02-06 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0004_auto_20190130_1949'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='feedback',
            unique_together={('min_value', 'max_value', 'indicator')},
        ),
    ]
