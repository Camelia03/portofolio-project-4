# Generated by Django 3.2.20 on 2023-08-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0021_alter_thread_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='edited_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
