# Generated by Django 3.2.20 on 2023-08-15 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0018_thread_edited_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='edited_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
