# Generated by Django 4.0 on 2021-12-23 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(default='No id', max_length=264)),
                ('video_title', models.CharField(default='No Title', max_length=264)),
                ('description', models.CharField(blank=True, default='No Description', max_length=500, null=True)),
                ('publishing_datetime', models.DateTimeField()),
                ('thumbnail_url_s', models.URLField(unique=True)),
                ('thumbnail_url_m', models.URLField(unique=True)),
                ('thumbnail_url_h', models.URLField(unique=True)),
                ('channel_title', models.CharField(default='No Title', max_length=264)),
            ],
        ),
    ]