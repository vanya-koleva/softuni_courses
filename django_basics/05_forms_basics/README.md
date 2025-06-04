# Forms Basics

## Web/HTML Forms

-   A mechanism for the client to send data to the server.

-   Example: the search bar on SoftUni

-   Main form parameters:

    -   action

        -   **where**: We provide a URL to which we want to send our data

            -   Default value → current URL

    -   method

        -   **how**: We specify the HTTP method for our request

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
            "employee_form": EmployeeForm(),
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

-   `is_valid()`

    -   Runs all validation (built-in and custom) on all the form fields

    -   It populates:

        -   **On success**: `form.cleaned_data` - A dictionary of validated and converted input data.

        -   **On failure**: `form.errors` - A dictionary of errors for fields that failed validation.

-   `form = EmployeeForm()` - Create a blank form.

    -   Used when we need an empty form (e.g., initial GET request).

-   `form = EmployeeForm(request.POST)` - Create a form instance and populate it with data from the request.

    -   Used when handling form submissions (e.g., validation on POST).

-   `form = EployeeForm(request.POST or None)` - If the user has made a POST request and there is data, then load the form with the data. Else, load an empty form.

    -   If POST data exists → `EmployeeForm(request.POST)`

    -   If no POST data → `EmployeeForm()`

## Workflow in the View

-   Give an empty form to the user.

-   When the user fills data into the form:

    -   validate it:

        -   if valid:

            -   save the cleaned_data

            -   redirect the user

        -   if not valid:

            -   give the user the form with the errors

## Form Field Arguments

-   `required`

    -   By default, each Field class in Django assumes that a value is required.

        -   If you pass an empty value, it will raise a `ValidationError`

-   `label`

-   `initial` - The initial value of the field.

-   `help_text`

## Widgets

-   The rendering of the form fields (the HTML).

-   Django uses default widgets according to the data type.

-   We can specify HTML attributes in the widgets' `attrs`

```python
first_name = forms.CharField(
    widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"})
)
```

## Working with Form Templates

-   Use Django's template variable syntax `{{ form }}` to render forms

    -   The output does not include the surrounding `<form>` tags, nor the submit button.

## ModelForm Class

-   Create forms directly from models.

-   Generates form fields based on your model's fields.

-   Provides `form.save()` method to create/update model instances.

```python
# models.py
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publish_date = models.DateField()

# forms.py
class BookForm(ModelForm):
    class Meta:
        model = Book  # Links form to model
        fields = '__all__'  # Includes all model fields
        # OR specify fields explicitly:
        # fields = ['title', 'author']
```

-   Field selection:

```python
class Meta:
    fields = ['title', 'author']  # Whitelist
    exclude = ['publish_date']     # Blacklist
```

