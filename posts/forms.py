from django import forms
from posts.models import Post

class PostForm(forms.Form):
    image = forms.ImageField(required=False)
    title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=100)

    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title.lower() == "javascript":
            raise forms.ValidationError("Javascrip is not allowed")
        return title
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if title and content and (title.lower() == content.lower()):
            raise forms.ValidationError("Title and content should be different")
        return cleaned_data