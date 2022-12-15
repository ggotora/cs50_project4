from django.forms import ModelForm, Textarea
from .models import Post 

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields = ["content"]
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 2, "class":"form-control"}),
            
        }