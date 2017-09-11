from django.db import models


class Article(models.Model):

    attr = models.CharField(max_length=32, default="Title")
    content = models.TextField(null=True)

    def __str__(self):
        return self.attr

