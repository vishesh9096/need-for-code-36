# Generated by Django 4.0.2 on 2022-07-27 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_queries_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queries',
            name='date',
        ),
    ]
