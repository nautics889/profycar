# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-10 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_picrel'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picrel',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='images/'),
        ),
    ]