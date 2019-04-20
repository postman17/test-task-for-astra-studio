from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from .models import BlogModel
from .forms import BlogForm

from .mixins import AjaxableResponseMixin


class BlogListView(ListView):
    model = BlogModel
    template_name = 'index.html'


class BlogCreateView(AjaxableResponseMixin, CreateView):
    model = BlogModel
    fields = ['message']


class BlogUpdateView(UpdateView):
    model = BlogModel
    template_name = 'update.html'
    form_class = BlogForm


class BlogDeleteView(DeleteView):
    model = BlogModel
    template_name = 'delete.html'
    success_url = reverse_lazy('index')
