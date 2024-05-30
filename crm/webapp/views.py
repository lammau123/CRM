from django.shortcuts import render
from .models import CustomerDto
from .forms import CustomerForm
from datetime import datetime

def home(request):
    return render(request, 'home.html', {})

def list_customer(request):
    context = {'customers': [
        CustomerDto(name='test1', phone='123-123-123', address='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        CustomerDto(name='test1', phone='123-123-123', address='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        CustomerDto(name='test1', phone='123-123-123', address='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        CustomerDto(name='test1', phone='123-123-123', address='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
    ]}
    return render(request, 'list-customer.html', context=context)

def create_customer(request):
    context = {"form": CustomerForm()}
    return render(request, "create-customer.html", context=context)
    