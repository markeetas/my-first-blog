from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
<<<<<<< HEAD
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
=======
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
>>>>>>> 228ca5dcb62c0c38c0fb92aac92c574ca4b27a8b

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
<<<<<<< HEAD
        return self.title
=======
        return self.title
>>>>>>> 228ca5dcb62c0c38c0fb92aac92c574ca4b27a8b
