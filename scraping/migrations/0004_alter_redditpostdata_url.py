# Generated by Django 4.0 on 2021-12-22 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0003_alter_redditpostdata_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redditpostdata',
            name='url',
            field=models.URLField(max_length=2000),
        ),
    ]
