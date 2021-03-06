# Generated by Django 4.0 on 2021-12-20 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedditPostData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('score', models.IntegerField()),
                ('post_id', models.IntegerField()),
                ('url', models.CharField(max_length=2000)),
                ('num_comments', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('post_body', models.CharField(max_length=40000)),
            ],
        ),
        migrations.CreateModel(
            name='RedditReplyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('post_id', models.IntegerField()),
                ('parent_id', models.IntegerField()),
                ('post_body', models.CharField(max_length=40000)),
            ],
        ),
        migrations.DeleteModel(
            name='RedditData',
        ),
    ]
