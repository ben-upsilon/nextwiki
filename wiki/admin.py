from django.contrib import admin

# Register your models here.

from .models import Article, Edit

admin.site.register(Article)
admin.site.register(Edit)
