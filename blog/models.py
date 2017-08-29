from django.db import models
from django.db.models import permalink
from django.utils import timezone


def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
