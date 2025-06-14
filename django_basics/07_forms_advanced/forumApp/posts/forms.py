from django import forms
from django.core.exceptions import ValidationError

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

    def clean_author(self):
        author = self.cleaned_data.get('author')

        if not author.isalpha():
            raise ValidationError('Author name must contain only letters')

        return author

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title.lower() in content.lower():
            raise ValidationError("The title shouldn't be included in the content.")

        return cleaned_data


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

