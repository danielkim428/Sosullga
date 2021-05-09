from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta

# Create your models here.
class Novel(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=10, null=True, blank=True)
    file = models.FileField(upload_to='novel/', null=True, blank=True)
    rating = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

class Reader(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"

class Setting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    dark = models.BooleanField(default=False)
    size = models.CharField(max_length=10, default=16)
    height = models.CharField(max_length=10, default=24)
    width = models.CharField(max_length=10, default=48)

    def __str__(self):
        return f"{self.user}"

class Marker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, blank=True, null=True)
    page = models.IntegerField(default=1)
    percent = models.IntegerField(default=0)
    time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.user} - {self.novel.title} - {self.page} ({self.percent}%)"

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, blank=True, null=True)
    page = models.IntegerField(default=1)
    time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.user} - {self.novel.title} - {self.page}"

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter_of", blank=True, null=True)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, related_name='comment_of', blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=50000)
    time = models.DateTimeField(default=datetime.now())

    def __str__ (self):
        return f"{self.author}"


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    solved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.title}"
