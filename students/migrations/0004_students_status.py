# Generated by Django 4.0.5 on 2022-12-21 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_remove_students_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
