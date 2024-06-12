from django.shortcuts import render
from .models import ContactDto, OpportunityDto
from .forms import ContactForm, OpportunityForm
from datetime import datetime
from django.contrib import messages
from .repository import repositories as repos
import logging
logger = logging.getLogger(__name__)

async def home(request):
    return render(request, 'home.html', {})

async def list_contact(request):
    logger.info('Starting list contacts.')
    context = {
        'contacts': await repos.get_contacts(),
        'header_names': ContactDto.get_header_names(),
        'field_names': ContactDto.get_field_names()
    }
    return render(request, 'list-contact.html', context=context)

async def add_contact(request):
    logger.info('Starting add contact.')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            logger.info('adding new contact passed validation.')
            # submit dto to the backend
            contact_dto = ContactDto(**form.cleaned_data, id = -1, created_at = datetime.now(), updated_at = datetime.now())
            messages.success(request, "Customer added successfully.")
            form = ContactForm()
        else:
            logger.error('adding new contact failed validation with error: {}'.format(form.errors.as_text()))
    else:
        logger.info('init a new ContactForm.')
        form = ContactForm()
        
    return render(request, "add-contact.html", context={'form': form})

async def edit_contact(request, id=0):
    contact_dto = await repos.get_contact_by_id(id)
    logger.info('Starting edit contact: {} {}'.format(contact_dto.first_name, contact_dto.last_name))
    if request.method == 'POST':
        form = ContactForm(request.POST, initial=contact_dto.to_dict())
        if form.is_valid():
            logger.info('Editing contact pass validation')
            # submit dto to the backend
            contact_dto.update(form)
            messages.success(request, "Contact updated successfully.")
        else:
            logger.error('Editing contact failed validation with error: {}'.format(form.errors.as_text()))
    else:
        logger.info('Init edit ContactForm: {} {}'.format(contact_dto.first_name, contact_dto.last_name))
        form = ContactForm(initial=contact_dto.to_dict())
        
    return render(request, "edit-contact.html", context={"form": form})
    
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
    logger.info('Starting list opportunity.')
    context = { 
               'opportunities': await repos.get_opportunities(),
               'header_names': OpportunityDto.get_header_names(),
               'field_names': OpportunityDto.get_field_names(),
            }
    return render(request, 'list-opportunity.html', context=context)

async def add_opportunity(request):
    logger.info('Starting add opportunity.')
    statuses = (*[(-1, '----select----')], *[(status.id, status.name) for status in await repos.get_opportunity_statuses()])
    users = (*[(-1, '----select----')], *[(user.id, user.username) for user in await repos.get_users()])
    contacts = (*[(-1, '----select----')], *[(contact.id, " ".join([contact.first_name, contact.last_name])) for contact in await repos.get_contacts()])
    intial_value = {'status': -1, 'user': -1, 'contact': -1}
    
    if request.method == 'POST':
        form = OpportunityForm(request.POST, initial=intial_value)
        form.fields['status'].choices = statuses
        form.fields['user'].choices = users
        form.fields['contact'].choices = contacts
        
        if form.is_valid():
            # submit dto to the backend
            logger.info('Adding a new opportunity passed validation.')
            contact_dto = OpportunityDto(**form.cleaned_data, id = -1, opened_at = datetime.now(), closed_at = datetime.now())
            messages.success(request, "Opportunity was added successfully.")
            form = OpportunityForm(initial=intial_value)
            form.fields['status'].choices = statuses
            form.fields['user'].choices = users
            form.fields['contact'].choices = contacts
        else:
            logger.error('Adding a new opportunity failed validation with errors: {}'.format(form.errors.as_text()))
    else:
        logger.info('Init a new opportunity form.')
        form = OpportunityForm(initial=intial_value)
        form.fields['status'].choices = statuses
        form.fields['user'].choices = users
        form.fields['contact'].choices = contacts
        
    return render(request, "add-opportunity.html", context={'form': form})

async def edit_opportunity(request, id=0):
    opportunity_dto = await repos.get_opportunity_by_id(id)
    logger.info('Starting edit opportunity: {}'.format(opportunity_dto.name))
    
    statuses = (*[(-1, '----select----')], *[(status.id, status.name) for status in await repos.get_opportunity_statuses()])
    users = (*[(-1, '----select----')], *[(user.id, user.username) for user in await repos.get_users()])
    contacts = (*[(-1, '----select----')], *[(contact.id, " ".join([contact.first_name, contact.last_name])) for contact in await repos.get_contacts()])
                
    if request.method == 'POST':
        form = OpportunityForm(request.POST, initial=opportunity_dto.to_dict())
        form.fields['status'].choices = statuses
        form.fields['user'].choices = users
        form.fields['contact'].choices = contacts
        if form.is_valid():
            logger.info('Editing an opportunity passed validation.')
            # submit dto to the backend
            opportunity_dto = opportunity_dto.update(form)
            messages.success(request, "Opportunity was added successfully.")
        else:
            logger.error('Editing the opportunity failed validation with errors: {}'.format(form.errors.as_text()))
    else:
        logger.info('Init the opportunty form.')
        form = OpportunityForm(initial=opportunity_dto.to_dict())
        form.fields['status'].choices = statuses
        form.fields['user'].choices = users
        form.fields['contact'].choices = contacts
        
    return render(request, "edit-opportunity.html", context={'form': form})
