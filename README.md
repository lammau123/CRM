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
- fontawesome
- Azure authentication and Authorization

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
crispy-bootstrap5
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

#### 5.1 Create webapp under django project
From command line creates under django project folder, run the below command

```cmd
python manage.py startapp webapp
```

The command above will create a sub webapp under the crm project.

#### 5.2 Register sub applications to django project
Wired sub applications which are included in the django project in settings.py under crm folder:
- webapp
- crispy_forms
- crispy_bootstrap5

```python
INSTALLED_APPS = [
    ...,
    
    'webapp.apps.WebappConfig',
    'crispy_forms',
    'crispy_bootstrap5',
]
```

#### 5.3 Create basic template files for the webapp
The web application includes base.html file, menu-items.html, and specific templates. 
- base.html is the basic template of the project, all specific template would extends from this template and creates its main content in the content area. 
- menu-items.html is included in the base.html and contains the menu function of the project.

![CRM diagram](/assets/images/base.png)

#### 5.4 Add javascript and css 
Under the webapp folder create the below files structure. app.js contains customered javascript function and styles.css contains customize css style, but they are empty now.

![CRM diagram](/assets/images/static.png)

#### 5.5 Add template files  
Under the webapp folder create the below files structure.

![CRM diagram](/assets/images/templates.png)

#### 5.6 Update templates content
Update the base.html template files to include:
- menu-items.html
- styles.css
- https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css
- https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css
- https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js
- app.js

base.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Bootstrap Vertical Collapse Navbar Layout</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
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
            {% include "menu-items.html" %}
          </div>
        </div>
        <div class="col py-3">{% block content %}{% endblock %}</div>
      </div>
    </div>
    <script src="{% static 'js/app.js' %}"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
  </body>
</html>
```

Update the menu-items.html 
```html
<ul
  class="nav nav-pills flex-column mb-sm-auto mb-0 align-items-center align-items-sm-start"
  id="menu"
>
  <li class="nav-item">
    <a href="#" class="nav-link align-middle px-0">
      <i class="fs-4 bi-house"></i>
      <span class="ms-1 d-none d-sm-inline"><i class="fa fa-home" aria-hidden="true"></i> &nbsp; Home</span>
    </a>
  </li>
  <li class="nav-item">
    <a href="/dashboard" class="nav-link align-middle px-0">
      <span class="ms-1 d-none d-sm-inline"><i class="fa fa-tachometer" aria-hidden="true"></i>&nbsp;
        Dashboard</span>
    </a>
  </li>
  <li class="nav-item">
    <a href="/customer" class="nav-link align-middle px-0">Customer</a>
  </li>
  <li class="nav-item">
    <a href="#" class="nav-link align-middle px-0">
      <span class="ms-1 d-none d-sm-inline">Task</span>
    </a>
  </li>
  <li class="nav-item">
    <a href="/opportunity" class="nav-link align-middle px-0">
      <span class="ms-1 d-none d-sm-inline">Opportunity</span>
    </a>
  </li>
</ul>
```

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
```

#### 6.3 Task model
```python
```

#### 6.4 Opportunity model
```python
```

## 7. Create list customer page
Under templates folder create new file list-customer.html template and add the below code:

```html
{% extends "base.html" %}

{% block content %}  
    <a href="customer/add" class="btn btn-primary btn-lg" tabindex="-1" role="button" aria-disabled="true">
        <i class="fa fa-plus" aria-hidden="true"></i>
    </a>
    <table class="table table-striped">
        <thead>
        <tr>
            <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">Address</th>
            <th scope="col">Email</th>
            <th scope="col">Phone</th>
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
            <td>{{customer.phone}}</td>
            <td>{{customer.created_at}}</td>
        </tr>
        {% endfor %}
        </tbody>
    </table>
{% endblock %}
```

Open views.py and add the below code

```python
def list_customer(request):
    context = {'customers': [
        CustomerDto(name='test1', phone='123-123-123', address='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        CustomerDto(name='test1', phone='123-123-123', address='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        CustomerDto(name='test1', phone='123-123-123', address='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        CustomerDto(name='test1', phone='123-123-123', address='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
    ]}
    return render(request, 'list-customer.html', context=context)
```

Create new urls.py under the webapp folder and add the below code

```python
from django.urls import path
from . import views

urlpatterns = [
    path('customer', views.list_customer, name='list-customer'),
]
```

#### 8 Run and test the app

```cmd
    python manage.py runserver
```

Open browser with url=http://localhost:8000/customer

Result
![CRM diagram](/assets/images/list-customer.png)

#### 13.2 Create create customer pageS
- Create CustomerForm class

```python
from django import forms

class CustomerForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    address = forms.CharField()
```

- Add new create-customer.html page

```html
{% extends "base.html" %}
{% load crispy_forms_tags %}
{% block content %}
    <div class="container">
    {% for message in messages %}
        {% if message.level == DEFAULT_MESSAGE_LEVELS.SUCCESS %}
            <p id="message-timer" class="alert alert-success float-center text-center message-text"> 
                <i class="fa fa-check" aria-hidden="true"></i> &nbsp; {{message}}
            </p>
        {% endif %}
    {% endfor %}
    <form method="POST" autocomplete="off">
        {% csrf_token %}
        {% for field in form %}
        <div class="row">
            <div class="col-xs-4">
                {{field|as_crispy_field}}
            </div>
        </div>
        {% endfor %}
        <div class="col-auto">
            <button type="submit" class="btn btn-primary mb-3">Create &nbsp;<i class="fa fa-check" aria-hidden="true"></i></button>
            <a href="/customer" class="btn btn-primary mb-3" role="button" aria-disabled="true">
                &nbsp;Cancel&nbsp;
            </a>
        </div>
        
    </form>
</div>
{% endblock %}
```

- Add create customer request handler to views.py

```python
def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            dto = CustomerDto(**form.cleaned_data, created_at = datetime.now(), updated_at = datetime.now())
            # submit dto to the backend
            messages.success(request, "Customer added successfully.")
            form = CustomerForm()
    else:
        form = CustomerForm()
        
    return render(request, "create-customer.html", context={'form': form})
```

Result
![CRM diagram](/assets/images/create-customer.png)

## 8. Implement Authentication and Authorization
: Use Django's built-in authentication system to manage user accounts and permissions.
## 9. Add Additional Features
Implement additional features like reporting, dashboards, and integrations with other services.

## 10. Test and Deploy
Thoroughly test the application and deploy it to a production server.
