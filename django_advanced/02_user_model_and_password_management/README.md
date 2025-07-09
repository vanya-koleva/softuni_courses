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

