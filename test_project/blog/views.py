from django.views.generic.list import ListView

from .models import BlogModel


class BlogListView(ListView):
    model = BlogModel
    template_name = 'index.html'
