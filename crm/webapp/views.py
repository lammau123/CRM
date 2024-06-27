from django.shortcuts import render
from .models import ContactDto, OpportunityDto, TaskDto
from .forms import ContactForm, OpportunityForm, TaskForm
from datetime import datetime
from django.contrib import messages
from .repository import repositories as repos
from django.conf import settings
import logging

logger = logging.getLogger('django')
ms_identity_web = settings.MS_IDENTITY_WEB

@ms_identity_web.login_required
def home(request):
    return render(request, 'home.html', {})

@ms_identity_web.login_required
def list_contact(request):
    logger.info('Starting list contacts.')
    context = {
        'contacts': repos.get_contacts(),
        'header_names': ContactDto.get_header_names(),
        'field_names': ContactDto.get_field_names()
    }
    return render(request, 'list-contact.html', context=context)

def add_contact(request):
    logger.info('Starting add contact.')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            logger.info('adding new contact passed validation.')
            # submit dto to the backend
            contact_dto = ContactDto(**form.changed_data_to_dict(), id = -1, created_at = datetime.now(), updated_at = datetime.now())
            messages.success(request, "Customer added successfully.")
            form = ContactForm()
        else:
            logger.error('adding new contact failed validation with error: {}'.format(form.errors.as_text()))
    else:
        logger.info('init a new ContactForm.')
        form = ContactForm()
        
    return render(request, "add-contact.html", context={'form': form})

def edit_contact(request, id=0):
    contact_dto = repos.get_contact_by_id(id)
    logger.info('Starting edit contact: {} {}'.format(contact_dto.first_name, contact_dto.last_name))
    if request.method == 'POST':
        form = ContactForm(request.POST, initial=contact_dto.to_dict())
        if form.is_valid():
            logger.info('Editing contact pass validation')
            # submit dto to the backend
            contact_dto.update(form.changed_data_to_dict())
            messages.success(request, "Contact updated successfully.")
        else:
            logger.error('Editing contact failed validation with error: {}'.format(form.errors.as_text()))
    else:
        logger.info('Init edit ContactForm: {} {}'.format(contact_dto.first_name, contact_dto.last_name))
        form = ContactForm(initial=contact_dto.to_dict())
        
    return render(request, "edit-contact.html", context={"form": form})
    
def list_opportunity(request):
    logger.info('Starting list opportunity.')
    context = { 
               'opportunities': repos.get_opportunities(),
               'header_names': OpportunityDto.get_header_names(),
               'field_names': OpportunityDto.get_field_names(),
            }
    return render(request, 'list-opportunity.html', context=context)

def add_opportunity(request):
    logger.info('Starting add opportunity.')
    intial_value = {'status': -1, 'user': -1, 'contact': -1}
    
    if request.method == 'POST':
        form = OpportunityForm(request.POST, initial=intial_value)
        form.load()
        
        if form.is_valid():
            # submit dto to the backend
            logger.info('Adding a new opportunity passed validation.')
            opportunity_dto = OpportunityDto(**form.changed_data_to_dict(), id=-1, opened_at = datetime.now(), closed_at = datetime.now())
            logger.info(opportunity_dto.to_dict())
            messages.success(request, "Opportunity was added successfully.")
            form = OpportunityForm(initial=intial_value)
            form.load()
        else:
            logger.error('Adding a new opportunity failed validation with errors: {}'.format(form.errors.as_text()))
    else:
        logger.info('Init a new opportunity form.')
        form = OpportunityForm(initial=intial_value)
        form.load()
        
    return render(request, "add-opportunity.html", context={'form': form})

def edit_opportunity(request, id=0):
    opportunity_dto = repos.get_opportunity_by_id(id)
    
    logger.info('Starting edit opportunity: {}'.format(opportunity_dto.name))
                
    if request.method == 'POST':
        form = OpportunityForm(request.POST, initial=opportunity_dto.to_ref_dict())
        form.load()
        
        if form.is_valid():
            logger.info('Editing an opportunity passed validation.')
            # submit dto to the backend
            opportunity_dto = opportunity_dto.update(form.changed_data_to_dict())
            messages.success(request, "Opportunity was added successfully.")
        else:
            logger.error('Editing the opportunity failed validation with errors: {}'.format(form.errors.as_text()))
    else:
        logger.info('Init the opportunty form.')
        form = OpportunityForm(initial=opportunity_dto.to_dict())
        form.load()
        
    return render(request, "edit-opportunity.html", context={'form': form})


def list_task(request):
    logger.info('Starting list tasks.')
    context = {
        'tasks': repos.get_tasks(),
        'header_names': TaskDto.get_header_names(),
        'field_names': TaskDto.get_field_names()
    }
    return render(request, 'list-task.html', context=context)

def add_task(request):
    logger.info('Starting add task.')
    intial_value = {}
    
    if request.method == 'POST':
        form = TaskForm(request.POST, initial=intial_value)
        form.load()
        
        if form.is_valid():
            # submit dto to the backend
            logger.info('Adding a new task passed validation.')
            task_dto = TaskDto(**form.changed_data_to_dict(), id=-1, opened_at = datetime.now(), closed_at = datetime.now())
            messages.success(request, "Task was added successfully.")
            form = TaskForm(initial=intial_value)
            form.load()
        else:
            logger.error('Adding a new task failed validation with errors: {}'.format(form.errors.as_text()))
    else:
        logger.info('Init a new task form.')
        form = TaskForm(initial=intial_value)
        form.load()
        
    return render(request, "add-task.html", context={'form': form})

def edit_task(request, id):
    task_dto = repos.get_task_by_id(id)
    
    logger.info('Starting edit task: {}'.format(task_dto.name))
                
    if request.method == 'POST':
        form = TaskForm(request.POST, initial=task_dto.to_ref_dict())
        form.load()
        
        if form.is_valid():
            logger.info('Editing an task passed validation.')
            # submit dto to the backend
            task_dto = task_dto.update(form.changed_data_to_dict())
            messages.success(request, "Task was added successfully.")
        else:
            logger.error('Editing the task failed validation with errors: {}'.format(form.errors.as_text()))
    else:
        logger.info('Init the opportunty form.')
        form = TaskForm(initial=task_dto.to_dict())
        form.load()
        
    return render(request, "edit-opportunity.html", context={'form': form})
