# Generated by Django 4.1.2 on 2023-04-19 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_lecture_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='day_of_week',
            field=models.CharField(choices=[('Monday', 'MONDAY'), ('Tuesday', 'TUESDAY'), ('Wednesday', 'WEDNESDAY'), ('Thursday', 'THURSDAY'), ('Friday', 'FRIDAY'), ('Saturday', 'SATURDAY'), ('Sunday', 'SUNDAY')], default='Monday', max_length=9),
            preserve_default=False,
        ),
    ]
