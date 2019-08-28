from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.TextField()
    created_at = models.DateField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    post = models.ForeignKey(Blog,on_delete=models.CASCADE) 
    content = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add= True)