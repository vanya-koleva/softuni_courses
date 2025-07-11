# User Model and Password Management

## Built-in Django User

-   User(AbstractUser)

    -   Can be found in the models of the `django.auth` app

    -   Table: `auth_users`

    -   We have access to it in every request via `request.user`

    -   Django allows us to customize the built-in user model on several levels

        -   We can **extend** it by inheriting from `AbstractUser`

        -   Or **fully replace** it by inheriting from `AbstractBaseUser`

    -   Inherits from `PermissionsMixin`, which provides:

        -   Superuser status handling

        -   User permissions and group management

        -   The `staff_member_required` decorator

    -   **`USERNAME_FIELD`** allows us to override the field that will be used as the primary credential

    -   **`email_user()`** allows us to send emails to users after configuring SMTP

    -   **`AnonymousUser`** - not a model but a class that overrides all attributes of the base class

    -   Provides two main functions:

        -   **`login`** – attaches a cookie for the authenticated user

        -   **`authenticate`** – checks whether the user’s credentials are valid

    -   **`get_user_model()`** – returns the currently active user model used in the application

## Login

-   Django's Built-in `LoginView`

-   When using `LoginView`, we get access to the following parameters:

    -   **`next`** - Helps redirect the user to the view they tried to access before logging in

    -   **`site`** - The URL of the website

## Register

-   We don't have a view for registration, but we do have a form

```py
class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


# settings.py - optional
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

 <form method="post" action="{% url 'login' %}{% if next %}?next={{ next }}{% endif %}">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Login</button>
 </form>
```

-   The form only works with Django's built-in User, but there is a way to change that

```py
   class CustomUserCreationForm(UserCreationForm):
       class Meta(UserCreationForm.Meta):
           model = get_user_model()  # Use the custom user model
           fields = ('username', 'email')
```

## Passwords

-   Use one-way hash
-   We have views for changing passwords

## Groups

-   `has_perm()`
-   `PermissionsMixin`
-   `permission_required()` – decorator

