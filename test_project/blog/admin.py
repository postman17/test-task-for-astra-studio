from django.contrib import admin

from .models import BlogModel


@admin.register(BlogModel)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['message', 'is_created']
