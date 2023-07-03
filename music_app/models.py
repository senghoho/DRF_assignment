from django.db import models

# Create your models here.

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    artist = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    year = models.IntegerField(default=0)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Track(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    album = models.ForeignKey(Album, blank=False, null=False, on_delete=models.CASCADE, related_name='tracks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album, blank=False, null=False, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, blank=False, null=False, on_delete=models.CASCADE)
    writer = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
