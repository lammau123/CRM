# Creating a CRM (Customer Relationship Management) web application

## 1. High-level architechture 
![CRM diagram](/assets/images/crm.png)

The above diagram depicts the CRM web application that is going to be built. 
Here are the technology stack used in the project:

## 2. Main features are supported in this web application
- customer management
- sales tracking
- task management
- reporting

## 3. Technology stack in the application
- DJango framework version 5.0.6
- django-bootstrap5
- django-crispy-forms
- azure ad authentication and authorization

## 4. Preparing Development Environment

#### 4.1 Install python

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

## 5. Set Up the Project
Create a new Django project and configure the necessary settings.

## 6. Create Models
Define the data models for your CRM, such as Customer, Contact, Task, Opportunity, etc.

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