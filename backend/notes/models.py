from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True

class Notes(models.Model):
    title = models.CharField(max_length=140, blank=True, default='')
    body = models.TextField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey('auth.User', related_name='notes', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
