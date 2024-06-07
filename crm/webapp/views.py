from django.shortcuts import render
from .models import ContactDto
from .forms import ContactForm
from datetime import datetime
from django.contrib import messages

list_of_contacts = [
        ContactDto(id=1, first_name='first', last_name='last', phone='123-123-123', company='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        ContactDto(id=1, first_name='first', last_name='last', phone='123-123-123', company='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        ContactDto(id=1, first_name='first', last_name='last', phone='123-123-123', company='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        ContactDto(id=1, first_name='first', last_name='last', phone='123-123-123', company='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        ContactDto(id=1, first_name='first', last_name='last', phone='123-123-123', company='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
    ]

contacts = {contact.id: contact for contact in list_of_contacts}


def home(request):
    return render(request, 'home.html', {})

def list_contact(request):
    context = {'contacts': list_of_contacts}
    return render(request, 'list-contact.html', context=context)

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

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # submit dto to the backend
            contact_dto = ContactDto(**form.cleaned_data, id = -1, created_at = datetime.now(), updated_at = datetime.now())
            messages.success(request, "Customer added successfully.")
            form = ContactForm()
    else:
        form = ContactForm()
        
    return render(request, "add-contact.html", context={'form': form})
    