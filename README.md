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
    
    'webapp',
]
```
#### 5.3 Create entry point for the webapp
Create new urls.py under the webapp folder and add the below code

```python
from django.urls import path

urlpatterns = [
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
## 6. Create Models
Define the data models for your CRM, such as Customer, Contact, Task, Opportunity, etc.
#### 6.1 Customer model

#### 6.2 Contact model

#### 6.3 Task model

#### 6.4 Opportunity model

## 7. Create Views and Templates
Implement views to handle HTTP requests and templates to render HTML pages.

## 8. Set Up URL Routing
Define URL patterns to map URLs to views.

## 9. Add Forms
Create forms for adding and editing CRM data.

## 10. Implement Authentication and Authorization
: Use Django's built-in authentication system to manage user accounts and permissions.
## 11. Add Additional Features
Implement additional features like reporting, dashboards, and integrations with other services.

## 12. Test and Deploy
Thoroughly test the application and deploy it to a production server.