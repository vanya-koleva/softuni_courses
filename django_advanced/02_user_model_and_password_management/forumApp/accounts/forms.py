from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


UserModel = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email')

        help_texts = {
            'username': '',
            'password': '', # has to go through the __init__ because it is dynamically created
            'email': '',
        }
