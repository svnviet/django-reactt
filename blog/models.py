import datetime

from django.db import models
from django.contrib.auth.models import User
from res_users.models import Customer


class Blog(models.Model):
    title = models.CharField(max_length=50, default="")
    storyline = models.TextField(default="")
    genres = models.CharField(max_length=100, default="")
    stars = models.CharField(max_length=255, default="")
    creators = models.CharField(max_length=255, default="")
    languages = models.CharField(max_length=100, default="")
    release_date = models.DateField(default=datetime.date.today)
    runtime = models.IntegerField(default=0)
    trailer = models.URLField(blank=True, default="")
    poster = models.ImageField(null=True, blank=True, upload_to="media")
    production_companies = models.CharField(max_length=255)

    def __str__(self):
        return self.title
