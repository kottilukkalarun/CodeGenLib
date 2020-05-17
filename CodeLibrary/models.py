from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
# Create your models here.
class ReferenceBook(models.Model):

    # article_manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    article_title = models.CharField(max_length=500)
    topicType = (
        ('Epiplex', 'Epiplex'),
        ('UiPath', 'UiPath'),
        ('Python','Python'),
        ('C#.net','C#.net'),
        ('HTML','HTML'),
        ('Bootstrap', 'Bootstrap'),
        ('Javascript', 'Javascript'),
    )
    article_topic_type = models.CharField(max_length=100, choices=topicType, default='Epiplex')
    article_content = models.TextField(editable=True)

    updated = (
        ('admin','Arun Kesavan'),
        ('user','Others'),
    )
    article_updated_by = models.CharField(max_length=500, choices=updated, default='admin')
    last_updated_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes  = models.IntegerField(default=0)

    def __str__(self):
        return self.article_title