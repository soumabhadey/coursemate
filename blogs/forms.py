from django import forms
from blogs.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = [ "author", "date_created", "tags" ]
        labels = {
            "body": "Body (Markdown): "
        }
        widgets = {
            'image': forms.FileInput(),
            "title": forms.Textarea(attrs={"rows": 2, "cols": 40, "placeholder": "Add title"}),
            "body": forms.Textarea(attrs={"rows": 20, "cols":50, "placeholder": "Write markdown"})
        }