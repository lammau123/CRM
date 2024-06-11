from django.shortcuts import render
from .models import ContactDto, OpportunityDto
from .forms import ContactForm, OpportunityForm
from datetime import datetime
from django.contrib import messages
from .repository import repositories as repos

async def home(request):
    return render(request, 'home.html', {})

async def list_contact(request):
    context = {
        'contacts': await repos.get_contacts(),
        'header_names': ContactDto.get_header_names(),
        'field_names': ContactDto.get_field_names()
    }
    return render(request, 'list-contact.html', context=context)

async def edit_contact(request, id=0):
    list_of_contacts = await repos.get_contacts()
    contacts = {contact.id: contact for contact in list_of_contacts}

    contact_dto = contacts[id]
    
    if request.method == 'POST':
        form = ContactForm(data=contact_dto.toDict())
        if form.is_valid():
            # submit dto to the backend
            messages.success(request, "Contact updated successfully.")
    else:
        form = ContactForm(initial=contact_dto.toDict())
        
    return render(request, "edit-contact.html", context={"form": form})

async def add_contact(request):
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
    
async def list_task(request):
    context = { 'tasks': await repos.get_tasks() }
    return render(request, 'list-task.html', context=context)

async def add_task(request):
    context = { 'tasks': await repos.get_tasks() }
    return render(request, 'list-task.html', context=context)

async def edit_task(request):
    context = { 'tasks': await repos.get_tasks() }
    return render(request, 'list-task.html', context=context)

async def list_opportunity(request):
    context = { 
               'opportunities': await repos.get_opportunities(),
               'header_names': OpportunityDto.get_header_names(),
               'field_names': OpportunityDto.get_field_names(),
            }
    return render(request, 'list-opportunity.html', context=context)

async def add_opportunity(request):
    if request.method == 'POST':
        form = OpportunityForm(request.POST)
        if form.is_valid():
            # submit dto to the backend
            contact_dto = OpportunityDto(**form.cleaned_data, id = -1, created_at = datetime.now(), updated_at = datetime.now())
            messages.success(request, "Opportunity was added successfully.")
            form = OpportunityForm()
    else:
        form = OpportunityForm()
        
    return render(request, "add-opportunity.html", context={'form': form})

async def edit_opportunty(request, id=0):
    opportunity_dto = await repos.get_opportunity_by_id(id)
    
    if request.method == 'POST':
        form = ContactForm(data=opportunity_dto.toDict())
        if form.is_valid():
            # submit dto to the backend
            messages.success(request, "Contact updated successfully.")
    else:
        form = ContactForm(initial=opportunity_dto.toDict())
        
    return render(request, "edit-opportunity.html", context={"form": form})