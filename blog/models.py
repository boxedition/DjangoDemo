from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post (models.Model):
    title = models.CharField(max_length=255)
    content= models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # Author -> on_delete will make sure that in the case of a USER gets DELETED,
    # the posts associated with the USER WILL also be DELETED
    author = models.ForeignKey(User, on_delete=models.CASCADE)