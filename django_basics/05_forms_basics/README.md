# Forms Basics

## Web/HTML Forms

-   A mechanism for the client to send data to the server.

-   Example: the search bar on SoftUni

-   Main form parameters:

    -   action

        -   We provide a URL to which we want to send our data

            -   Default value → current URL

    -   method

        -   We specify the HTTP method for our request

            -   Default value → `GET`

        -   With `GET`, the form information is sent as a query string in the URL

        -   With `POST`/`PUT`, the information is sent in the body of the request

## Form Fields

-   Forms collect information through input fields

-   Fields must have a `name` attribute so we can read them in the backend

-   We can see the submitted data in the **request payload** in the browser

## Input Types

-   `email`
-   `range`
-   `number`
-   `text`
-   `password`
-   `url`
-   `hidden`
-   `radio`
-   `checkbox`

## Textarea

-   `input` is for single-line text

-   `textarea` is for multi-line text

## Dropdowns

```html
<select>
    <option value="1">Gaming</option>
    <option value="2">Reading</option>
</select>
```

## Forms in Django

-   We create them in `forms.py`

```python
class EmployeeForm(forms.Form):
    first_name = forms.CharField(
        max_length=35,
        required=True,
    )
```

-   In the template:

```html
<form action="{% url 'index' %}" method="post">
    {{ employee_form }} 
    {% csrf_token %}
    <button>Send</button>
</form>
```

-   In the view:

```python
def index(request):
    if request.method == "GET":
        context = {
            "employee_form": EmployeeForm,
        }
        return render(request, "web/index.html", context)
    else:
        print(request.POST)  # Get the data but without any validation
        form = EmployeeForm(request.POST)

        if form.is_valid():  # Starts validation, returns boolean
            print(form.cleaned_data["first_name"])
            return redirect('index')
        else:
            context = {
                "employee_form": form,  # Pass form with errors
            }
            return render(request, "web/index.html", context)
```

