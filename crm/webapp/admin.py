from django.contrib import admin

# Register your models here.
# crm/admin.py

from .models import Customer, Opportunity, Task, Contact

admin.site.register(Customer)
admin.site.register(Opportunity)
admin.site.register(Task)
admin.site.register(Contact)
