# Generated by Django 4.1.2 on 2022-10-27 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('width', models.IntegerField(blank=True, default=0, null=True)),
                ('height', models.IntegerField(blank=True, default=0, null=True)),
                ('color', models.IntegerField(default=0)),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
                ('albumId', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
