import datetime
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


class News(models.Model):
    title = models.CharField(max_length=50)
    text_news = RichTextUploadingField()
    author_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    created_date = models.DateTimeField(default=timezone.now)
    is_public = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title


def publish(self):
    self.published_date = timezone.now()
    self.save()


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    comment_text = RichTextUploadingField()
    author_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.author_name