# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    picrel = models.ImageField(blank=True, upload_to='picrelies/', help_text='150x150px', verbose_name='Ссылка картинки')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title

    def image_img(self):
        if self.picrel:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100" /></a>'.format(self.image.url)
        else:
            return "None"

    picrel.short_description = "Picture"
    picrel.allow_tags = True