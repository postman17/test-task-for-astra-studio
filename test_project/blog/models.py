from django.db import models
from django.urls import reverse_lazy


class BlogModel(models.Model):

    message = models.TextField()
    is_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Blog model'
        verbose_name_plural = 'Blog models'

    def __str__(self):
        return f'{self.message[:20]}'

    def get_absolute_url(self):
        return reverse_lazy('index')
