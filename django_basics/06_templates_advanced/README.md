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

