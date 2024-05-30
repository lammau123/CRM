# Creating a CRM (Customer Relationship Management) web application

## 1. High-level architechture 
![CRM diagram](/assets/images/crm.png)

The above diagram depicts the CRM web application that is going to be built. 
Here are the technology stack used in the project:

## 2. Main features are supported in this web application
- Customer management
- Sales tracking
- Task management
- Reporting

## 3. Technology stack in the application
- dJango framework version 5.0.6
- django-bootstrap5
- django-crispy-forms
- azure ad authentication and authorization

## 4. Preparing Development Environment

#### 4.1 Install python

Download link: https://www.python.org/downloads/
Version: 3.12.3

#### Setup project

From commandline 
#### 1. Create a CRM folder

```cmd
mkdir CRM
cd CRM
```

#### 2. Create virtual environment

```cmd
python -m venv venv
```

#### 3. Activate virtual environment

```cmd
venv\Scripts\activate
```

#### 4. Create text file requirement.txt and add the below required package

```cmd
django==5.0.6
django-bootstrap5
django-crispy-forms
```

#### 5. Intall required packages

```cmd
pip install -r requirment.txt
```

#### 6. Create django project

```cmd
django-admin startproject crm
```

#### 7. Run the server

```cmd
cd crm
python manage.py migrate
python manage.py runserver
```

#### 8. Check the application

Open browser with url http://localhost:8000/

## 5. Set Up the Project
Create a new Django app and configure the necessary settings. Django project includes one or more sub applications under django project.
- register webapp to django project
- Register webapp to django project
- Create entry point for the webapp
- Register the entry of the webapp to the django project

#### 5.1 Create webapp under django project
From command line creates under django project folder, run the below command

```cmd
python manage.py startapp webapp
```

#### 5.2 Register webapp to django project
Open the settings.py and update the below code

```python
INSTALLED_APPS = [
    ...,
    
    'webapp.apps.WebappConfig',
]
```
#### 5.3 Write your first view
Open views.py and add the below code

```python
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', context={})
```

Create templates folder under webapp and create new home.html template file in templates folder

```html
<h1>This is CRM application</h1>
```

Create new urls.py under the webapp folder and add the below code

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home')
]
```

#### 5.4 Register the entry of the webapp to the django project
Open then file urls.py under the folder crm and add the below code

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls'))
]
```

#### 5.5 run and test the app

```cmd
    python manage.py runserver
```

Open browser with url=http://localhost:8000

## 6. Create Models
Define the data models for your CRM, such as Customer, Contact, Task, Opportunity, etc.
Open the models.py under the webapp folder and add the models to it.

#### 6.1 Customer model
```python
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class CustomerDto:
    name: str
    email: str
    phone: str
    address: str
    created_at: datetime
    updated_at: datetime
```

#### 6.2 Contact model
```python
class Contact(models.Model):
    customer = models.ForeignKey(Customer, related_name='contacts', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
```

#### 6.3 Task model
```python
class Task(models.Model):
    customer = models.ForeignKey(Customer, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(User, related_name='tasks', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
```

#### 6.4 Opportunity model
```python
class Opportunity(models.Model):
    customer = models.ForeignKey(Customer, related_name='opportunities', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    stage = models.CharField(max_length=50, choices=[
        ('Qualification', 'Qualification'),
        ('Needs Analysis', 'Needs Analysis'),
        ('Proposal', 'Proposal'),
        ('Negotiation', 'Negotiation'),
        ('Closed Won', 'Closed Won'),
        ('Closed Lost', 'Closed Lost'),
    ])
    close_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(User, related_name='opportunities', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
```

## 7. Activating models
That small bit of model code gives Django a lot of information. With it, Django is able to

Create a database schema (CREATE TABLE statements) for this app.
Create a Python database-access API for accessing Question and Choice objects.

```cmd
python manage.py makemigrations polls
```

Create SQL statement

```python
python manage.py sqlmigrate polls
```

Now, run migrate again to create those model tables in your database

```python
python manage.py migrate
```

## 8. Create admin user
First create a user who can login to the admin site. Run the following command

```cmd
python manage.py createsuperuser
```

## 9. Explore the free admin functionality
Run the server and open url http://localhost:8000/admin

## 10. Create CRM general page layout
- Create foundation base.html template contains common elements and structure for other templates to inherit and build upon
- Create menu-items.html template for the left menu items
- Create home.html page extends the base.html template

#### 10.1 Create foundation base.html template contains common elements and structure for other templates to inherit and build upon
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Bootstrap Vertical Collapse Navbar Layout</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"/>
  </head>
  <body>
    <!-- Banner -->
    <div class="bg-primary text-white text-center p-3">
      <h1>Customer Relationship Management.</h1>
    </div>
    <div class="container-fluid">
      <div class="row flex-nowrap">
        <div class="col-auto col-md-3 col-xl-2 px-sm-2 px-0 bg-dark">
          <div class="d-flex flex-column align-items-center align-items-sm-start px-3 pt-2 text-white min-vh-100">
            <a href="/" class="d-flex align-items-center pb-3 mb-md-0 me-md-auto text-white text-decoration-none">
              <span class="fs-5 d-none d-sm-inline">Menu</span>
            </a>
            {% include "menu-items.html" %}
          </div>
        </div>
        <div class="col py-3">{% block content %}{% endblock %}</div>
      </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
  </body>
</html>
```

#### 10.2 Create menu-items.html template for the left menu items
```html
<ul
  class="nav nav-pills flex-column mb-sm-auto mb-0 align-items-center align-items-sm-start"
  id="menu"
>
  <li class="nav-item">
    <a href="#" class="nav-link align-middle px-0">
      <i class="fs-4 bi-house"></i>
      <span class="ms-1 d-none d-sm-inline">Home</span>
    </a>
  </li>
  <li class="nav-item">
    <a href="/dashboard" class="nav-link align-middle px-0">
      <i class="fs-4 bi-house"></i>
      <span class="ms-1 d-none d-sm-inline">Dashboard</span>
    </a>
  </li>
  <li class="nav-item">
    <a href="/customer" class="nav-link align-middle px-0">
      <i class="fs-4 bi-house"></i>
      <span class="ms-1 d-none d-sm-inline">Customer</span>
    </a>
  </li>
  <li class="nav-item">
    <a href="#" class="nav-link align-middle px-0">
      <i class="fs-4 bi-house"></i>
      <span class="ms-1 d-none d-sm-inline">Task</span>
    </a>
  </li>
  <li class="nav-item">
    <a href="/opportunity" class="nav-link align-middle px-0">
      <i class="fs-4 bi-house"></i>
      <span class="ms-1 d-none d-sm-inline">Opportunity</span>
    </a>
  </li>
</ul>
```

#### 10.3 Create home.html page extends the base.html template

```html
{% extends "base.html" %}

{% block content %}
    Content Area1 ...
{% endblock %}
```

Result
![CRM diagram](/assets/images/home.png)
## 12. Set Up URL Routing
Define URL patterns to map URLs to views.

## 13. Create CRUD customer function
#### 13.1 List customer page
Under webapp folder add new font awesome css

```html
  <head>
    ...
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    ...
  </head>
```

Under webapp folder add new list-customer.html template and add the below code

```html
{% extends "base.html" %}

{% block content %}
    <button type="button" class="btn btn-lg btn-primary" disabled><i class="fa fa-plus" aria-hidden="true"></i></button>
    <table class="table table-striped">
        <thead>
        <tr>
            <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">Address</th>
            <th scope="col">Email</th>
            <th scope="col">Created Date</th>
        </tr>
        </thead>
        <tbody>
        {% for customer in customers %}
        <tr>
            <th scope="row">{{forloop.counter}}</th>
            <td>{{customer.name}}</td>
            <td>{{customer.address}}</td>
            <td>{{customer.email}}</td>
            <td>{{customer.created_at}}</td>
        </tr>
        {% endfor %}
        </tbody>
    </table>
{% endblock %}
```

Under webapp folder open the views.py and add the below code

```python
from .models import CustomerDto

def list_customer(request):
    context = {'customers': [
        CustomerDto(name='test1', phone='123-123-123', address='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        CustomerDto(name='test1', phone='123-123-123', address='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        CustomerDto(name='test1', phone='123-123-123', address='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        CustomerDto(name='test1', phone='123-123-123', address='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
    ]}
    return render(request, 'list-customer.html', context=context)
```

Under the webapp folder open urls.py and add the below code

```python
urlpatterns = [
    ...
    path('customer', views.list_customer, name='list-customer'),
]
```
Result
![CRM diagram](/assets/images/list-customer.png)

#### 13.2 Add customer page
- Install crispy-bootstrap5

```txt
```
- Update settings.py

```python
```

- Create CustomerForm class

```python
from django import forms

class CustomerForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    address = forms.CharField()
    created_at = forms.DateField()
    updated_at = forms.DateField()
```

- Add new create-customer.html page

```html
{% extends "base.html" %}

{% block content %}
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Save">
    </form>
{% endblock %}
```

- Add create customer request handler to views.py

```python
def create_customer(request):
    context = {"form": CustomerForm()}
    return render(request, "create-customer.html", context=context)
```

#### 13.3 Update customer page

#### 13.4 Delete customer page

## 13. Add Forms
Create forms for adding and editing CRM data.

## 14. Implement Authentication and Authorization
: Use Django's built-in authentication system to manage user accounts and permissions.
## 15. Add Additional Features
Implement additional features like reporting, dashboards, and integrations with other services.

## 16. Test and Deploy
Thoroughly test the application and deploy it to a production server.
