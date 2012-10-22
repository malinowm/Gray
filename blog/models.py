from django.db import models
from datetime import datetime

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.tag

class Comment(models.Model):
    poster = models.CharField(max_length=30)
    pub_date = models.DateTimeField('Posted on', default = datetime.now)
    content = models.TextField()

    def __unicode__(self):
        return self.poster

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Posted on', default = datetime.now)
    content = models.TextField()
    tag = models.ManyToManyField(Tag)
    postno = models.PositiveIntegerField()
    comments = models.ForeignKey(Comment, blank=True, null=True)

    def __unicode__(self):
        return self.title

