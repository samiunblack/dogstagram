from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'description', 'hashtags']
        
    def save(self, commit=True):
        post = super(PostForm, self).save(commit=False)
        if commit:
                post.save()
        return post