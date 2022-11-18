from django.contrib import admin

# Register your models here.
from .models import Blog


# admin.site.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_ja', 'created_datetime', 'updated_datetime')
    list_display_links = ('id', 'title_ja')


admin.site.register(Blog, BlogAdmin)
