from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='children',
                               on_delete=models.CASCADE)
    url = models.CharField(max_length=255, blank=True)
    named_url = models.CharField(max_length=255, blank=True)
    menu_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url
