from django import forms

from posts.mixins import ReadOnlyFieldsMixin
from posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'language': forms.RadioSelect(
                attrs={'class': 'radio-select'},
            )
        }

        error_messages = {
            'author': {
                'max_length': "Hey, that's too much",
            }
        }


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(ReadOnlyFieldsMixin, PostBaseForm):
    pass


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={'placeholder': 'Search...'}
        )
    )

