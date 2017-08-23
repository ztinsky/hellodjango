from django.db import models
from cgi import maxlen
from django.template.defaultfilters import title
from email.quoprimime import body_check
from unicodedata import category
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return 'Category:'+self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return 'Tag:'+self.name
    
class Post(models.Model):
    title=models.CharField(max_length=70)
    body=models.TextField()
    created_time=models.DateTimeField()
    modified_time=models.DateTimeField()
    excerpt=models.CharField(max_length=200,blank=True)
    category=models.ForeignKey(Category)
    tags=models.ManyToManyField(Tag)
    author=models.ForeignKey(User)
    def __str__(self):
        return 'Post:'+self.title