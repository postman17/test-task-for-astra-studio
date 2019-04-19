from django.db import models


class BlogModel(models.Model):

    message = models.TextField()
    is_created = models.DateTimeField(auto_now_add=True)
