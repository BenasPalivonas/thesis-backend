# Generated by Django 4.1.2 on 2023-04-17 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_name_student_full_name_student_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='default', max_length=255),
            preserve_default=False,
        ),
    ]