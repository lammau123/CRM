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

mkdir develop
cd develop

#### 2. Create virtual environment

python -m venv venv

#### 3. Activate virtual environment

venv\Scripts\activate

#### 4. Create text file requirement.txt and add the below required package

django=5.0.6

#### 5. Intall required packages

pip install -r requirment

#### 6. Create django project

django-admin startproject crm

#### 7. Run the server

cd crm
python manage.py runserver

#### 8. Check the application

Open browser with url http://localhost:8000/

#### 9. Create an app in django project

python manage.py startapp webapp

![Project structure](/assets/images/crm.png)