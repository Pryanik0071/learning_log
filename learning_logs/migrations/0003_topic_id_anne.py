# Generated by Django 2.2 on 2022-08-19 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='id_anne',
            field=models.TextField(null=True),
        ),
    ]
