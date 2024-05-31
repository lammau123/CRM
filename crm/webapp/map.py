from .models import CustomerDto
from .forms import CustomerForm
from datetime import datetime

def customer_form_to_dto(form: CustomerForm):
    dto = CustomerDto(
        name = form.cleaned_data['name'],
        email = form.cleaned_data['email'],
        phone = form.cleaned_data['phone'],
        address = form.cleaned_data['address'],
        created_at = datetime.now(),
        updated_at = datetime.now()
    )
    return dto