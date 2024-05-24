from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from .form import CreateUserForm, LoginForn, CreateCustomerForm, UpdateRecordForm
from .models import Record
import logging

logger = logging.getLogger(__name__)

# home page
def home(request):
    return render(request, 'webapp/index.html')

# register page
def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect('my-login')
        
    context = {'form': form}
    return render(request, 'webapp/register.html', context=context)   

def user_login(request):
    login = LoginForn()
    
    if request.method == 'POST':
        login = LoginForn(request, data=request.POST)
        if login.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
        messages.success(request, "Account created successfully.")
       
    context = {'form': login} 
    return render(request, 'webapp/login.html', context=context)    

@login_required(login_url='user-login')
def dashboard(request):
    my_record = Record.objects.all()
    context = {'records': my_record}
    
    return render(request, 'webapp/dashboard.html', context=context)

def user_logout(request):
    auth.logout(request)
    messages.success(request, "Logout success!")
    return redirect("user-login")

@login_required(login_url='user-login')
def create_customer(request):
    record = CreateCustomerForm()
    
    if request.method == 'POST':
        record = CreateCustomerForm(request.POST)    
        if record.is_valid():
            record.save()   
            messages.success(request, "Your new Customer was created!")
            return redirect('dashboard')
    context = {'form': record}
    return render(request, 'webapp/create-customer.html', context=context)

@login_required(login_url='user-login')
def singular_record(request, pk):
    try:
        record = Record.objects.get(id=pk)
    except Record.DoesNotExist:
        logger.warning(f"Attempted to access non-existent record with ID: {pk}")
        return render(request, 'webapp/404.html', status=404)
    context={'record': record}
    return render(request, 'webapp/view-record.html', context=context)

@login_required(login_url='user-login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was updated!")
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'webapp/update-record.html', context=context)

@login_required(login_url='user-login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, "Your record was deleted!")
    return redirect("dashboard")
