# Generated by Django 4.1.2 on 2023-04-27 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_assignment_lecturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='core.student'),
        ),
    ]
