from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from .models import BlogModel
from .forms import BlogForm


class BlogListView(ListView):
    model = BlogModel
    template_name = 'index.html'
    paginate_by = 5


class BlogCreateView(CreateView):
    form_class = BlogForm
    model = BlogModel
    template_name = 'create.html'


class BlogUpdateView(UpdateView):
    model = BlogModel
    template_name = 'update.html'
    form_class = BlogForm


class BlogDeleteView(DeleteView):
    model = BlogModel
    template_name = 'delete.html'
    success_url = reverse_lazy('index')
