# Django REST Advanced

## Types of Serializers

-   **Serializer**

    -   This is the base class for creating serializers. You manually define the fields and how the data should be processed.

```py
    from rest_framework import serializers

    class UserSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=100)
        email = serializers.EmailField()
        is_active = serializers.BooleanField()

    # Serializing data:
    user_data = {
        "username": "john",
        "email": "john@example.com",
        "is_active": True
    }
    serializer = UserSerializer(data=user_data)
    if serializer.is_valid():
        print(serializer.validated_data)
```

-   **ModelSerializer**

    -   `ModelSerializer` is a simplified version of Serializer that automatically creates fields based on a Django model. It saves time when serializing model data.

```py
   from rest_framework import serializers
   from myapp.models import User

   class UserSerializer(serializers.ModelSerializer):
       class Meta:
           model = User
           fields = ['username', 'email', 'is_active']
```

-   **ListSerializer**

    -   `ListSerializer` is used for serializing lists of objects. It is usually used internally by Django REST Framework when serializing multiple objects but can also be defined manually.

```py
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)

class UserListSerializer(serializers.ListSerializer):
    child = UserSerializer()

data = [
    {"username": "john"},
    {"username": "jane"}
]
serializer = UserListSerializer(data=data)
if serializer.is_valid():
    print(serializer.validated_data)
```

-   **HyperlinkedModelSerializer**

    -   `HyperlinkedModelSerializer` is similar to `ModelSerializer`, but instead of using `PrimaryKeyRelatedField` for relationships, it uses `HyperlinkedIdentityField` to provide URL links to other resources.

```py
from rest_framework import serializers
from myapp.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_active']
```

-   **SlugRelatedField**

    -   `SlugRelatedField` is used for relationships by linking other models through their unique fields (e.g., a slug field).

```py
from rest_framework import serializers
from myapp.models import Post, Category

class PostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ['title', 'content', 'category']
```

-   **PrimaryKeyRelatedField**

    -   This serializer uses the primary key for relationships between models.

```py
from rest_framework import serializers
from myapp.models import Post, Category

class PostSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ['title', 'content', 'category']
```

-   **StringRelatedField**

    -   `StringRelatedField` displays relationships as strings, based on the `str()` method of the related model.

```py
   from rest_framework import serializers
   from myapp.models import Post

   class PostSerializer(serializers.ModelSerializer):
       category = serializers.StringRelatedField()

       class Meta:
           model = Post
           fields = ['title', 'content', 'category']
```

-   **SerializerMethodField**

    -   This field type allows you to define a method in the serializer that returns data in serialized form.

```py
from rest_framework import serializers
from myapp.models import User

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'email', 'full_name']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
```

-   **HiddenField**

    -   A field used to pass values that are not displayed in the serialization (e.g., values that are auto-filled).

```py
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ['text', 'created_by']
```

## Generic Views

-   We can combine them, i.e., we can have a `RetrieveDestroyView`, which includes `get` and `delete`.

## Actions

-   A template for creating URLs in REST.

-   Example: We have books, and each book can have a comment.

-   Incorrect: `api/books/4` – where 4 is the ID of the book.

-   **Correct**: `api/books/4/comment` – this is called an action. This way, there’s no confusion about what the ID belongs to.

## Authentication

-   `rest_framework.authtoken`

-   An app that contains a view called `ObtainAuthToken`.

    -   Here, we can generate a token for an existing user.

-   Login

```py
class LoginAPIView(token_views.ObtainAuthToken)
   pass
```

-   Register

```py
 from django.contrib.auth import get_user_model
 from rest_framework import serializers

 UserModel = get_user_model()

 class RegisterSerializer(serializers.ModelSerializer):
     password = serializers.CharField(write_only=True)  # Prevent password from being read

     class Meta:
         model = UserModel
         fields = ['username', 'email', 'password']  # Adjust fields based on your User model

     def create(self, validated_data):
         # Use the create_user method to create a user
         user = UserModel.objects.create_user(
             username=validated_data['username'],
             email=validated_data['email'],
             password=validated_data['password']  # create_user automatically handles hashing
         )
         return user

 from django.contrib.auth import get_user_model
 from rest_framework import generics
 from rest_framework.response import Response
 from rest_framework import status

 UserModel = get_user_model()

 class RegisterApiView(generics.CreateAPIView):
     queryset = UserModel.objects.all()
     serializer_class = RegisterSerializer
```

## Permissions

-   We can use Django mixins, but it's more common to use **permission classes**:

    -   `IsAuthenticated`
    -   `AllowAny`
    -   `IsAdminUser`
    -   `IsAuthenticatedOrReadOnly`
    -   `BasePermission` (for creating custom permissions)

```py
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Custom permission to only allow owners of an object to access or modify it.
    """
    def has_object_permission(self, request, view, obj):
        # Assumes the object has an 'owner' attribute. You can adjust this as needed.
        return obj.owner == request.user

class MyModelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = [IsOwner]  # Use the custom permission
```

