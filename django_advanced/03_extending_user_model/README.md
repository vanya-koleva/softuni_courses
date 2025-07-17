# Extending the User Model

`AUTH_USER_MODEL = 'path.to.my.model'`

## Why do we inherit from `AbstractUser` and not `User`?

-   If we inherit from a non-abstract model, we get a 1-to-1 relationship.

-   Whereas, if it's abstract, we get the **fields directly in the same table**.

## `AbstractUser` vs `AbstractBaseUser`

-   `AbstractUser` is the user model we’re familiar with — the one Django uses by default. It inherits from `AbstractBaseUser`.

-   `AbstractBaseUser` only contains two fields: `password` and `last_login`.

## Ways to Extend the User Model

### 1. Via Proxy

**Pros:**

-   We can add methods and metadata while continuing to use Django’s built-in model.

-   No need to rewrite the Django Auth system.

**Cons:**

-   We can’t add custom fields.

---

### 2. By Inheriting from `AbstractUser` or `AbstractBaseUser`

**Pros:**

-   We can add our own custom fields.

-   No need to rewrite the Django Auth system.

**Cons:**

-   Harder to migrate to another authentication model in the future (e.g., switching from Django Sessions to JWT).

---

### 3. By Creating a Profile Model that Inherits from `User`

-   Creating a profile for each user via a **One-to-One** relationship.

**Pros:**

-   We can add custom fields.

-   Easier migration to another authentication model in the future (e.g., switching from Django Sessions to JWT).

**Cons:**

-   We have to rewrite the Django Auth system.

**This can be done in two ways:**

-   Inheriting from the built-in user model.

-   Creating our own user model.

-   We will need to modify the register platform

```py
      class CustomUserCreationForm(UserCreationForm):
        profile_field = forms.FieldType()

        class Meta(UserCreationForm.Meta):
            model = get_user_model()  # Use the custom user model
            fields = ('username', 'email')

        def save(self, commit=True):
            user = super().save(commit=commit)

            profile = Profile(
                user=user,
                age=self.cleaned_data["age"]
            )

            if commit:
                profile.save()

         return user
```

## User with `AbstractBaseUser`

**Step 1: Create a model and a manager**

```py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
```

**Step 2: Configure settings**

```py
AUTH_USER_MODEL = 'accounts.CustomUser'
```

**Step 3: Modify the User Creation Form**

-   In `accounts/forms.py`, import `get_user_model()` and use it to define the form class:

```py
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()  # Dynamically get the user model
        fields = ('email', 'first_name', 'last_name')
```

**Step 4: Update the Registration View**

-   Ensure your registration view is correctly set up to use the CustomUserCreationForm

-   In `accounts/views.py`:

```py
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    form_class = CustomUserLoginForm
    template_name = 'accounts/login.html'
```

**Step 5: Admin**

-   After creating a custom user model, you also need to configure the Django admin to manage users via the admin interface.

-   In your `accounts/admin.py`, register your custom user model with the Django admin interface. You need to create a custom ModelAdmin class to specify how the model should be displayed in the admin interface.

-   In `accounts/admin.py`:

```py
   from django.contrib import admin
   from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
   from django.contrib.auth import get_user_model
   from django.utils.translation import gettext_lazy as _
   from .forms import CustomUserCreationForm

   CustomUser = get_user_model()

   class CustomUserAdmin(BaseUserAdmin):
       add_form = CustomUserCreationForm
       form = CustomUserCreationForm
       model = CustomUser
       list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
       list_filter = ('is_staff', 'is_active')
       fieldsets = (
           (None, {'fields': ('email', 'password')}),
           (_('Personal Info'), {'fields': ('first_name', 'last_name')}),
           (_('Permissions'), {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
           (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
       )
       add_fieldsets = (
           (None, {
               'classes': ('wide',),
               'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_active')}
           ),
       )
       search_fields = ('email',)
       ordering = ('email',)

   admin.site.register(CustomUser, CustomUserAdmin)
```

## Signals

-   Publish-Subscribe Pattern

-   Types of signals:

    -   model

    -   request

    -   management

    -   etc...

-   When a certain event happens, specific code should be executed.

```py
   # accounts/models.py
   from django.conf import settings
   from django.db import models
   from django.contrib.auth import get_user_model

   class Profile(models.Model):
       user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
       bio = models.TextField(blank=True)
       location = models.CharField(max_length=100, blank=True)

       def __str__(self):
           return self.user.email

   # accounts/signals.py

   from django.db.models.signals import post_save
   from django.dispatch import receiver
   from django.conf import settings
   from .models import Profile

   @receiver(post_save, sender=settings.AUTH_USER_MODEL)
   def create_profile(sender, instance, created, **kwargs):
       if created:
           Profile.objects.create(user=instance)

   # accounts/apps.py

   from django.apps import AppConfig

   class AccountsConfig(AppConfig):
       default_auto_field = 'django.db.models.BigAutoField'
       name = 'accounts'

       def ready(self):
           import accounts.signals
```

