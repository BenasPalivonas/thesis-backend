# Generated by Django 4.1.2 on 2023-04-20 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_lecturesubject_alter_lecture_day_of_week_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='student_groups',
            field=models.ManyToManyField(to='core.studentgroup'),
        ),
    ]
