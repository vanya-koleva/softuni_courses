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

