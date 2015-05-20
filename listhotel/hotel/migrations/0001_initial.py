# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description_text', models.CharField(max_length=200)),
                ('image_galery', models.ImageField(default=b'pic_folder/None/no-img.jpg', upload_to=b'pic_folder/')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('logo', models.ImageField(default=b'pic_folder/None/no-img.jpg', upload_to=b'pic_folder/')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField()),
                ('hotel', models.ForeignKey(to='hotel.Hotel')),
            ],
        ),
        migrations.AddField(
            model_name='galery',
            name='hotel',
            field=models.ForeignKey(to='hotel.Hotel'),
        ),
    ]
