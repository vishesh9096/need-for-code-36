# Generated by Django 2.2.12 on 2020-04-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200419_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
