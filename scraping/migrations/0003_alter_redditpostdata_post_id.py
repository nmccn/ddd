# Generated by Django 4.0 on 2021-12-22 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_redditpostdata_redditreplydata_delete_redditdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redditpostdata',
            name='post_id',
            field=models.CharField(max_length=20),
        ),
    ]
