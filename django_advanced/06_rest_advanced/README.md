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

