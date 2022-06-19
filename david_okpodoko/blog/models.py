from typing import Text
from unicodedata import name
from django.db import models

# Create your models here.

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField(max_length=200)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL)
    Created_date = models.DateTimeField(max_length=200)
    Published_date = models.DateTimeField(max_length=200)
        
    def __str__(self):
        return self.name
    def __str__(self):
            return self.Title
    def __str__(self):
            return self.Text
    # def __str__(self):
            # return self.Author
    def __str__(self):
           return self.Created_date
    def __str__(self):
            return self.Published_date

   
