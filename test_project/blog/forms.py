from django import forms

from .models import BlogModel


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = [
            'message',
        ]
        widgets = {
            'message': forms.Textarea(
                attrs={'class': 'form-control', 'rows': '5'}
            )
        }