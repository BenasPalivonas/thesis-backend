# Generated by Django 4.1.2 on 2023-04-20 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_assignment_lecturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='lecturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='core.lecturer'),
        ),
    ]