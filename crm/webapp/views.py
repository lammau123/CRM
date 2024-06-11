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
    contact_dto = await repos.get_contact_by_id(id)
    
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
    statuses = [(-1, '----select----')]
    statuses.extend([(status.id, status.name) for status in await repos.get_opportunity_statuses()])
    users = [(-1, '----select----')]
    users.extend([(user.id, user.username) for user in await repos.get_users()])
    contacts = [(-1, '----select----')]
    contacts.extend([(contact.id, " ".join([contact.first_name, contact.last_name])) for contact in await repos.get_contacts()])
    intial_value = {'status': -1, 'user': -1, 'contact': -1}
    
    if request.method == 'POST':
        form = OpportunityForm(request.POST)
        if form.is_valid():
            # submit dto to the backend
            contact_dto = OpportunityDto(**form.cleaned_data, id = -1, created_at = datetime.now(), updated_at = datetime.now())
            messages.success(request, "Opportunity was added successfully.")
            form = OpportunityForm(initial=intial_value)
            form.fields['status'].choices = statuses
            form.fields['user'].choices = users
            form.fields['contact'].choices = contacts
    else:
        form = OpportunityForm(initial=intial_value)
        form.fields['status'].choices = statuses
        form.fields['user'].choices = users
        form.fields['contact'].choices = contacts
        
    return render(request, "add-opportunity.html", context={'form': form})

async def edit_opportunity(request, id=0):
    opportunity_dto = await repos.get_opportunity_by_id(id)
    
    if request.method == 'POST':
        form = OpportunityForm(data=opportunity_dto.toDict())
        if form.is_valid():
            # submit dto to the backend
            messages.success(request, "Contact updated successfully.")
    else:
        form = OpportunityForm(initial=opportunity_dto.toDict())
        
    return render(request, "edit-opportunity.html", context={"form": form})