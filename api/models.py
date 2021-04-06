from django.db import models
from urllib.parse import urlparse

# Create your models here.


class Shortener(models.Model):
    url = models.URLField(max_length=800)
    domain_shortened_domain = models.CharField(max_length=300)

    def __str__(self):
        return self.domain_shortened_domain

    def save(self, *args, **kwargs):
        domain = urlparse(self.url).netloc
        self.domain_shortened_domain = f'{domain}/{domain[::3]}'
        super(Shortener, self).save(*args, **kwargs)