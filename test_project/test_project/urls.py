from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.views import (
    BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BlogListView.as_view(), name='index'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('update/<pk>', BlogUpdateView.as_view(), name='update'),
    path('delete/<pk>', BlogDeleteView.as_view(), name='delete')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)