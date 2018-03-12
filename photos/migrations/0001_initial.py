# Generated by Django 2.0.2 on 2018-03-05 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('image', models.ImageField(height_field='height', upload_to='', width_field='width')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]