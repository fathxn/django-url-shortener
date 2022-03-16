from django.db import models
from random import choice, choices
from string import ascii_letters
from django.conf import settings

# Create your models here.
class Link(models.Model):
    longurl = models.URLField()
    shorturl = models.URLField(blank=True, null=True)

    def shortener(self):
        while True:
            random_strings = ''.join(choices(ascii_letters,k=6))
            newUrl = settings.HOST_URL+'/'+random_strings

            if not Link.objects.filter(shorturl=newUrl).exists():
                break

        return newUrl

    def save(self, *args, **kwargs):
        if not self.shorturl:
            newUrl = self.shortener()
            self.shorturl = newUrl
        return super().save(*args, **kwargs)