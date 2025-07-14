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

