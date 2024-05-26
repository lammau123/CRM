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
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
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

## 9. Make the crm app modifiable in the admin
Open the webapp/admin.py file, and edit it to look like this

```python
from .models import Customer, Opportunity, Task, Contact

admin.site.register(Customer)
admin.site.register(Opportunity)
admin.site.register(Task)
admin.site.register(Contact)
```

## 10. Explore the free admin functionality
Run the server and open url http://localhost:8000/admin

## 11. Create Views and Templates
Implement views to handle HTTP requests and templates to render HTML pages.

## 12. Set Up URL Routing
Define URL patterns to map URLs to views.

## 13. Add Forms
Create forms for adding and editing CRM data.

## 14. Implement Authentication and Authorization
: Use Django's built-in authentication system to manage user accounts and permissions.
## 15. Add Additional Features
Implement additional features like reporting, dashboards, and integrations with other services.

## 16. Test and Deploy
Thoroughly test the application and deploy it to a production server.