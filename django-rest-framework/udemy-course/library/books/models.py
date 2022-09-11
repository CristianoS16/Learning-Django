from uuid import uuid4

from django.db import models


class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    published_company = models.CharField(max_length=255)
    creat_at = models.DateField(auto_now=False, auto_now_add=True)
