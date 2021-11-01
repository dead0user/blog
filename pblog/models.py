from typing import Any
from django.db import models
from django.contrib.auth.models import User
from martor.models import MartorField

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1)
    update_on = models.DateTimeField(auto_now=True)
    intro = models.TextField()
    content = MartorField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self) -> str:
        return self.title
