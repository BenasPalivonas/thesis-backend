# Generated by Django 4.1.2 on 2023-04-20 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_assignment_lecturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='lecturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='core.lecturer'),
        ),
    ]