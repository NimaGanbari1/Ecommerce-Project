# Generated by Django 3.2 on 2023-09-22 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('avatar', models.ImageField(blank=True, upload_to='categories', verbose_name='avatar')),
                ('is_active', models.BooleanField(default=True, verbose_name='is enable')),
                ('slug', models.SlugField(max_length=100, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('1', 'PRODUCT'), ('2', 'QUESTION'), ('3', 'BRAND')], default='1', max_length=15)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Category.category', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'categories',
            },
        ),
    ]
