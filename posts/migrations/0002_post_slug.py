# Generated by Django 2.0.2 on 2018-03-05 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
    ]
