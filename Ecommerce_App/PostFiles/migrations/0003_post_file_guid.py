# Generated by Django 3.2 on 2024-07-06 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostFiles', '0002_delete_article_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_file',
            name='guid',
            field=models.CharField(blank=True, default='', max_length=40, unique=True),
        ),
    ]
