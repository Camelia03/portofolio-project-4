# Generated by Django 3.2.20 on 2023-08-15 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0016_auto_20230815_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upvote',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upvotes', to='forum.thread'),
        ),
    ]
