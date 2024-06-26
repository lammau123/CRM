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
- javascript/jquery

## 4. Preparing Development Environment

#### 4.1. Install python

Download link: https://www.python.org/downloads/
Version: 3.12.3

#### 4.2. Setup project

From commandline 
- Create a CRM folder

```cmd
mkdir CRM
cd CRM
```

- Create virtual environment

```cmd
python -m venv venv
```

- Activate virtual environment

```cmd
venv\Scripts\activate
```

- Create text file requirement.txt and add the below required package

```cmd
django==5.0.6
django-bootstrap5
django-crispy-forms
crispy-bootstrap5
```

- Intall required packages

```cmd
pip install -r requirment.txt
```

- Create django project

```cmd
django-admin startproject crm
```

- Run the server

```cmd
cd crm
python manage.py migrate
python manage.py runserver
```

- Check the application

Open browser with url http://localhost:8000/

## 5. Set Up the Project
Create a new Django app and configure the necessary settings. Django project includes one or more sub applications under django project.

#### 5.1. Create webapp under django project
From command line creates under django project folder, run the below command

```cmd
python manage.py startapp webapp
```

The command above will create a sub webapp under the crm project.

#### 5.2. Register sub applications to django project
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

#### 5.3. Create basic template files for the webapp
The web application includes base.html file, menu-items.html, and specific templates. 
- base.html is the basic template of the project, all specific template would extends from this template and creates its main content in the content area. 
- menu-items.html is included in the base.html and contains the menu function of the project.

![CRM diagram](/assets/images/base.png)

#### 5.4. Add javascript and css 
Under the webapp folder create the below files structure. app.js contains customered javascript function and styles.css contains customize css style, but they are empty now.

![CRM diagram](/assets/images/static.png)

#### 5.5. Add template files  
Under the webapp folder create the below files structure.

![CRM diagram](/assets/images/templates.png)

#### 5.6. Update templates content
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

#### 6.1. ContactDto model
```python
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class ContactDto:
    id: int
    last_name: str
    first_name: str
    email: str
    phone: str
    company: str
    created_at: datetime
    updated_at: datetime

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def toDict(self):
        return {
            "last_name": self.last_name, 
            "first_name": self.first_name, 
            "email": self.email, 
            "phone": self.phone, 
            "company": self.company
        }
```

#### 6.2. TaskTypeDto model

```python
@dataclass(frozen=True)
class TaskTypeDto:
    name: str
    
    def __str__(self):
        return self.name

    def toDict(self):
        return { "name": self.name }
```

#### 6.3. TaskStatusDto model

```python
@dataclass(frozen=True)
class TaskStatusDto:
    name: str
    
    def __str__(self):
        return self.name

    def toDict(self):
        return { "name": self.name }
```

#### 6.4. TaskDto model

```python
@dataclass(frozen=True)
class TaskDto:
    title: str
    opportunity_id: int
    due_date: datetime
    type_id: int
    status_id: int

    def __str__(self):
        return self.title

    def toDict(self):
        return {
            "title": self.title, 
            "opportunity": self.opportunity_id, 
            "due_date": self.due_date, 
            "type_id": self.type_id, 
            "status_id": self.status_id 
        }
```

#### 6.5. OpportunityStatusDto model

```python
@dataclass(frozen=True)
class OpportunityStatusDto:
    name: str
    
    def __str__(self):
        return self.name
    
    def toDict(self):
        return { "name": self.name }
```

#### 6.6. OpportunityDto model

```python
@dataclass(frozen=True)
class OpportunityDto:
    name: str
    amount: int
    user_id: int
    contact_id: int
    status_id: int
    open_date: datetime
    close_date: datetime
    
    def __str__(self):
        return self.name
    
    def toDict(self):
        return {
            "name": self.name, 
            "amount": self.amount, 
            "user_id": self.user_id, 
            "contact_id": self.contact_id, 
            "status_id": self.status_id, 
            "open_date": self.open_date,
            "close_date": self.close_date
        }
```

## 7. Create entry points

- Create new urls.py under the webapp folder and add the below code

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home, name='home'),
    path('contact', views.list_contact, name='list-contact'),
    path('contact/<int:id>/edit', views.edit_contact, name='edit-contact'),
    path('contact/add', views.add_contact, name='add-contact'),
]

```

## 8. CRUD Contact
#### 8.1. List Contact

- Under templates folder create new file list-contact.html template and add the below code:

```html
{% extends "base.html" %}
{% block content %}  
    <a href="{% url 'add-contact' %}" class="btn btn-primary btn-lg" tabindex="-1" role="button" aria-disabled="true">
        <i class="fa fa-plus" aria-hidden="true"></i>
    </a>
    <table class="table table-striped">
        <thead>
        <tr>
            <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">Company</th>
            <th scope="col">Email</th>
            <th scope="col">Phone</th>
            <th scope="col">Created Date</th>
            <th scope="col">&nbsp;</th>
        </tr>
        </thead>
        <tbody>
        {% for contact in contacts %}
        <tr>
            <th scope="row">{{forloop.counter}}</th>
            <td>{{contact.first_name}} {{contact.last_name}}</td>
            <td>{{contact.company}}</td>
            <td>{{contact.email}}</td>
            <td>{{contact.phone}}</td>
            <td>{{contact.created_at}}</td>
            <td><a href="{% url 'edit-contact' contact.id %}"><i class="fa fa-edit"></i></a></td>
        </tr>
        {% endfor %}
        </tbody>
    </table>
{% endblock %}
```

- Open views.py and add the below code

```python
list_of_contacts = [
        ContactDto(id=1, first_name='first', last_name='last', phone='123-123-123', company='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        ContactDto(id=1, first_name='first', last_name='last', phone='123-123-123', company='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        ContactDto(id=1, first_name='first', last_name='last', phone='123-123-123', company='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        ContactDto(id=1, first_name='first', last_name='last', phone='123-123-123', company='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        ContactDto(id=1, first_name='first', last_name='last', phone='123-123-123', company='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
    ]

contacts = {contact.id: contact for contact in list_of_contacts}

def list_contact(request):
    context = {'contacts': list_of_contacts}
    return render(request, 'list-contact.html', context=context)
```

![CRM diagram](/assets/images/list-contact.png)

#### 8.2. Create Contact
- Under templates folder create new file add-contact.html template and add the below code:

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
        <fieldset>
            <legend>Add Contact</legend>
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
                <a href="{% url 'list-contact' %}" class="btn btn-primary mb-3" role="button" aria-disabled="true">
                    &nbsp;Cancel&nbsp;
                </a>
            </div>
        </fieldset>
    </form>
</div>
{% endblock %}
```

- Open views.py and add the below code

```python
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # submit dto to the backend
            messages.success(request, "Customer added successfully.")
            form = ContactForm()
    else:
        form = ContactForm()
        
    return render(request, "add-contact.html", context={'form': form})
```

![CRM diagram](/assets/images/add-contact.png)

#### 8.3. Edit Contact

- Under templates folder create new file edit-contact.html template and add the below code:

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
            <button type="submit" class="btn btn-primary mb-3">Update &nbsp;<i class="fa fa-check" aria-hidden="true"></i></button>
            <a href="{% url 'list-contact' %}" class="btn btn-primary mb-3" role="button" aria-disabled="true">
                &nbsp;Cancel&nbsp;
            </a>
        </div>
        
    </form>
</div>
{% endblock %}
```

- Open views.py and add the below code

```python
def edit_contact(request, id=0):
    contact_dto = contacts[id]
    
    if request.method == 'POST':
        form = ContactForm(data=contact_dto.toDict())
        if form.is_valid():
            # submit dto to the backend
            messages.success(request, "Contact updated successfully.")
    else:
        form = ContactForm(initial=contact_dto.toDict())
        
    return render(request, "edit-contact.html", context={"form": form})
```

#### 8.4. Run and test the app

```cmd
    python manage.py runserver
```

Open browser with url=http://localhost:8000/customer

![CRM diagram](/assets/images/edit-contact.png)


- When Contact is added successfully, then a message "Contact added successfully." shows up at the top of created customer form. To hide this message after showing for some seconds. Open app.js page and add the below code:

```javascript
function hideMessage(){
    document.getElementById("message-timer").style.display = 'none';
}

setTimeout(hideMessage, 5000);
```

![CRM diagram](/assets/images/edit-contact.png)

## 9. Implement Authentication and Authorization

## 10. Add Additional Features
Implement additional features like reporting, dashboards, and integrations with other services.

## 11. Test and Deploy
Thoroughly test the application and deploy it to a production server.


Certainly! Implementing the described approach involves the following steps:

1. **Set Up Azure AD B2C**:
   - If you haven't already, create an Azure AD B2C tenant in your Azure portal.
   - Configure your B2C policies for sign-up, sign-in, and profile editing.

2. **External System Integration**:
   - Identify the external system (CRM or customer loyalty database) that will serve as the source of truth for customer data.
   - Ensure that the external system has APIs or connectors that allow you to retrieve and update customer data.

3. **Custom Policies in Azure AD B2C**:
   - Create custom policies in Azure AD B2C to handle the interaction with the external system.
   - Define custom claims transformations to map data between Azure AD B2C and the external system.

4. **User Flow Configuration**:
   - Set up user flows (e.g., sign-up, sign-in) in Azure AD B2C.
   - Configure the user flows to call the custom policies that interact with the external system.

5. **Authentication and Data Retrieval**:
   - When a user signs up or signs in, Azure AD B2C will authenticate them.
   - During the authentication process, the custom policies will retrieve additional customer data from the external system using APIs or connectors.

6. **Token Issuance and Claims**:
   - Azure AD B2C will issue tokens (e.g., ID tokens, access tokens) containing claims.
   - Customize the claims issuance policy to include relevant customer data from the external system as claims in the tokens.

7. **Application Integration**:
   - Integrate your application with Azure AD B2C for authentication.
   - When your application receives tokens, it can extract customer data from the claims.

Remember that the specifics of implementation depend on your application's architecture, the external system you're using, and your business requirements. Consult Azure AD B2C documentation and consider seeking professional guidance for a detailed implementation tailored to your needs. 😊

Certainly! In Azure Active Directory B2C (Azure AD B2C), custom policies allow you to create your own user journeys for complex identity scenarios that go beyond what predefined user flows offer. Let's dive into how you can integrate external systems using custom policies:

1. **Custom Policies Overview**:
   - Custom policies are configuration files that define the behavior of your Azure AD B2C tenant.
   - They allow you to edit and extend identity tasks beyond the standard user flows.
   - Custom policies can orchestrate trust between entities using protocols like OpenID Connect, OAuth, SAML, and even REST API-based system-to-system claims exchanges¹.

2. **Starter Pack**:
   - Azure AD B2C provides a custom policy starter pack with prebuilt policies to get you started quickly. These include:
     - **LocalAccounts**: Enables local accounts (username/password) only.
     - **SocialAccounts**: Enables social (or federated) accounts only.
     - **SocialAndLocalAccounts**: Allows both local and social accounts.
     - **SocialAndLocalAccountsWithMFA**: Supports social, local, and multifactor authentication options.
   - You can find additional samples in the Azure AD B2C GitHub repository for various scenarios like local account enhancements, MFA, user interface improvements, and more¹.

3. **Claims and Data Exchange**:
   - Claims play a crucial role in custom policies. They temporarily store data during policy execution.
   - You can collect claims from users during sign-up or profile editing flows.
   - Claims can be received from external identity providers or sent via custom REST APIs.
   - Customize your claims schema to declare the specific data you need¹.

4. **Integration with External Systems**:
   - Define your custom policy by creating multiple XML files that refer to each other hierarchically.
   - Within the custom policy, integrate your business logic to build the desired user experiences.
   - For external system integration, you can:
     - Use REST API communication to exchange data with the external system.
     - Extend functionality within the extension policy or relying party policy².

Remember that the specifics of your implementation will depend on your organization's requirements and the external system you're integrating with. Feel free to explore the custom policy starter pack and adapt it to your needs! 😊👍¹²

Source: Conversation with Copilot, 6/21/2024
(1) Azure Active Directory B2C custom policy overview. https://learn.microsoft.com/en-us/azure/active-directory-b2c/custom-policy-overview.
(2) User flows and custom policies in Azure Active Directory B2C - Azure AD .... https://learn.microsoft.com/en-us/azure/active-directory-b2c/user-flow-overview.
(3) External System Integration Settings - Fortinet. https://help.fortinet.com/fsiem/6-7-5/Online-Help/HTML5_Help/Integration-settings.htm.