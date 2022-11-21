from django.db import models


# Create your models here
class Category(models.Model):
    name = models.CharField('Category', max_length=50)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title_en = models.CharField('title_en', blank=False, null=False, max_length=150)
    title_ja = models.CharField('title_ja', blank=False, null=False, max_length=150)
    text_en = models.TextField('text_en', blank=True)
    text_ja = models.TextField('text_ja', blank=True)
    created_datetime = models.DateTimeField('create_day', auto_now_add=True)
    updated_datetime = models.DateTimeField('updata_day', auto_now=True)

    def __str__(self):
        return self.title_ja

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'
