# Templates Advanced

## Template Inheritance

-   Allows us to extend an HTML file.

-   We can use it for custom styles on each page: `{% block styles %}{% endblock %}` - placed in the header.

-   **The child template**:

    -   Overrides blocks.

    -   Cannot have content outside of the blocks.

    -   Place `{% extends %}` **FIRST** in child templates.

    -   Use `{{ block.super }}` to add to the parent content instead of replacing it.

```python
# base.html
<html>
   <h1>Hello</h1>
   {% block content %}
   {% endblock %}
</html>


# my-extending-file.html
{% extends 'base.html' %}

{% block content %}
   <p>Extending code</p>
{% endblock %}
```

## Template Including

-   To reuse a single HTML file in many places, we can embed/inject it into another HTML file:

```django
{% include 'reusable-file.html' %}
```

-   We can **pass parameters** to the included template, which can be accessed like context data.

    -   Use `with` to pass variables:

```django
{% include 'reusable-file.html' with name="Hello" %}
```

-   By default, included templates inherit parent context.

-   `only` - Restricts context to **explicitly passed variables only**. No access to parent context.

```django
{% include 'reusable-file.html' with name="Hello" only %}
```

-   Add `ignore missing` to suppress errors if template doesn't exist.

```django
{% include 'optional-banner.html' ignore missing %}
```

## Custom Filters

-   Create a module in our app that **must** be named `templatetags`.

-   Create a Python file inside `templatetags` and define the filter:

```python
from django import template

register = template.Library()

@register.filter(name='custom_title')
def custom_title(value):
    """Capitalizes the first letter of each word, except for specified words"""
    exceptions = ['and', 'or', 'the', 'in', 'on', 'at', 'to', 'with', 'a', 'an']
    words = value.split()
    result = []
    for word in words:
        if word.lower() in exceptions and len(result) != 0:
            result.append(word.lower())
        else:
            result.append(word.capitalize())
    return ' '.join(result)
```

-   Load the filter in the HTML file:

```django
{% load my_file_name %}
```

## Custom Tags

-   Simple Tag – returns a string:

```python
from django import template

register = template.Library()

@register.simple_tag
def simple_tag_example():
    return "This is a simple tag"
```

-   Inclusion Tag – returns an HTML string based on a template:

```python
   from django import template

   register = template.Library()

   @register.inclusion_tag('user_info.html', takes_context=True)
   def user_info(context, user, extra_info):
       return {
           'user': user,
           'extra_info': extra_info,
           'request': context['request']
       }

   <div class="user-info">
       <h2>User Information</h2>
       <p>Username: {{ user.username }}</p>
       <p>Email: {{ user.email }}</p>
       <p>Extra Info: {{ extra_info }}</p>
   </div>

   {% load my_tags %}

   <div>
       {% user_info user "Additional details about the user" %}
   </div>
```

-   Tag – returns a Template Node with a render function

```python
from django import template
from django.template import Node

register = template.Library()

class UppercaseNode(Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        return output.upper()

@register.tag(name="uppercase")
def do_uppercase(parser, token):
    nodelist = parser.parse(('enduppercase',))
    parser.delete_first_token()
    return UppercaseNode(nodelist)
```

## Bootstrap

-   [Link](https://getbootstrap.com/)

