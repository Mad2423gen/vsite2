from django.db import models


# Create your models here.
class Blog(models.Model):
    title_en = models.CharField(blank=False, null=False, max_length=150)
    title_ja = models.CharField(blank=False, null=False, max_length=150)
    text_en = models.TextField(blank=True)
    text_ja = models.TextField(blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
