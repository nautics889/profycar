# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from PIL import *
from django.contrib import admin
from .models import Post

admin.site.register(Post)