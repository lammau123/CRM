# CRM Web Application
![CRM diagram](/assets/images/crm.png)

The above diagram depicts the CRM web application that is going to be built. 
Here are the technology stack used in the project:

1. DJango framework version 5.0.6
2. PostgresSQL database

#### Install python

Download link: https://www.python.org/downloads/
Version: 3.12.3

#### Setup project

From commandline 
#### 1. Create a development folder

```cmd
mkdir develop
cd develop
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
django=5.0.6
```

#### 5. Intall required packages

```cmd
pip install -r requirment
```

#### 6. Create django project

```cmd
django-admin startproject crm
```

#### 7. Run the server

```cmd
cd crm
python manage.py runserver
```

#### 8. Check the application

Open browser with url http://localhost:8000/

#### 9. Create an app in django project

```cmd
python manage.py startapp webapp
```

![Project structure](/assets/images/project_structure.png)

The entry point of django project is configured in the urls.py file at the project level as the code below:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
]
```

Open the settings.py under crm folder and register the webapp in the INSTALLED_APPS array

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'webapp',
]
```

#### 10. Configured entry point for webapp in django project and add webapp entry point to the django project.

Create new urls.py under the webapp folder and add the below code into it.

```python
urlpatterns = [
    # entry point for webapp will be inserted here later
]
```

Add this entry point into the urls.py under crm folder as the code below:

```python
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls'))
]
```

#### 11. Create a request handler for home page

The webapp application recieves requests from users via web browser and django webapp handles it and returns a html page back to web brower. the returned html pages are configured as html template under webapp folder of the webapp application.

Create a templates folder under webapp folder and add index.html file and add the below code to it.

```html
<h1>This is home page of the CRM project</h1>
```

Open the views.py under webapp folder and add the code below:

```python
def home(request):
    return render(request, 'webapp/index.html', context={})
```

Update urls.py under webapp folder with the code below

```python
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

Open browser with url: http://localhost:8000, the home page show up the in the browser.

#### 12. Define template page structure

base.html template page defines the crm page structure. this page is extended from specific pages which are created later.
```html
{% load static %}
<!DOCTYPE html>

<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>CRM Project</title>
  </head>
  <body>
    <!-- Create NAV bar here -->
    {% include "webapp/navbar.html" %}
    <div class="container">
        <br />
        <h3>Notification message shows here</h3>

        {% block content %}
            <!-- Content of the page-->
        {% endblock %}
    </div>
  </body>
</html>
```

navbar.html template page
```html
<nav>
    <h2>Navigation menu shows here</h2>  
</nav>
```

index.html template page
```html
{% extends "webapp/base.html" %} 

{% block content %}
    <body>
        <div><h3>Content shows here</h3></div>
    </body>
{% endblock %}

```
Run and test to see the result

#### 13. Adding style sheet and javascript to the base.html template file

```html
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>CRM Project</title>
        <link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/flatly/bootstrap.min.css"/>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    <body>
        .....
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
    </body>
```

#### 14. Create layout for the navbar.html template
Replace the content of of navbar.html with the below code

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-primary justify-content-center">
    <a class="navbar-brand main-heading" href="{% url 'home' %}">CRM Project</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse text-center" id="navbarNav">
      <ul class="navbar-nav mr-auto">
          {% if user.is_authenticated %}
              <li class="nav-item">          
                  <a class="nav-link" href="{% url '' %}">Dashboard &nbsp; <i class="fa fa-home" aria-hidden="true"></i> </a>
              </li>
              &nbsp;     &nbsp;     &nbsp; 
              <li class="nav-item">      
                  <a class="nav-link" href="{% url '' %}">Sign out &nbsp; <i class="fa fa-sign-out" aria-hidden="true"></i> </a>
              </li>
          {% else %}
              <li class="nav-item">
                  <a class="nav-link" href="{% url '' %}">Register</a>
              </li>
              <li class="nav-item">
                  <a class="nav-link" href="{% url '' %}">Login</a>
              </li>
          {% endif %}
      </ul>
    </div>
</nav>
```
#### 15. Create layout for the Notification message
In the base.html template file replace the code 
```html
<h3>Notification message shows here</h3>
```
by
```html
<p id="message-timer" class="alert alert-success float-center text-center message-text"> 
    <i class="fa fa-check" aria-hidden="true"> &nbsp; This is notification message </i>
</p>
```
#### 16. Create layout for the index.html template
Replace the content in the index.html template with the below code

```html
{% block content %}
    <body>
        <br>
        <br>

        <div class="text-center">
            <h3>Simple CRM project demontration</h3>
            <br>
            <h5> Keep track of your records effectively!!</h5>
            <hr>
            <br>
            <a class="btn btn-primary" href="{% url 'register' %}">Create Your Account </a>
        </div>
    </body>
{% endblock %}
```