from django.contrib import admin

from django.contrib import admin
from .models import Post, ZigZagPost

admin.site.register(Post)
admin.site.register(ZigZagPost)