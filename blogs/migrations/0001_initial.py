# Generated by Django 4.1.3 on 2022-11-18 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=150)),
                ('title_ja', models.CharField(max_length=150)),
                ('text_en', models.TextField(blank=True)),
                ('text_ja', models.TextField(blank=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
