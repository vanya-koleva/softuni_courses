from django import forms

from posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class SearchForm(PostBaseForm):
    pass
