# Generated by Django 4.1.2 on 2023-04-30 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_assignment_venue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='created_by_lecturer',
            new_name='lecturer',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='created_by_student',
        ),
    ]
