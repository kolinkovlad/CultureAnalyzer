# Generated by Django 2.1.5 on 2019-01-22 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('tutors', '0003_question_category_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(db_column='question_id',
                                    on_delete=django.db.models.deletion.CASCADE,
                                    to='tutors.Question'),
        ),
        migrations.AlterField(
            model_name='categoryquestion',
            name='parent_category',
            field=models.ForeignKey(blank=True, db_column='parent_id',
                                    null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    to='tutors.CategoryQuestion'),
        ),
    ]
