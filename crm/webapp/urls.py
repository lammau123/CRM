"""
URL configuration for crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from ms_identity_web.django.msal_views_and_urls import MsalViews

msal_urls = MsalViews(settings.MS_IDENTITY_WEB).url_patterns()

urlpatterns = [
    path('dashboard', view=views.home, name='dashboard'),
    path('', view=views.home, name='index'),
    path('contact', views.list_contact, name='list-contact'),
    path('contact/<int:id>/edit', views.edit_contact, name='edit-contact'),
    path('contact/add', views.add_contact, name='add-contact'),
    
    path('task', views.list_task, name='list-task'),
    path('task/<int:id>/edit', views.edit_task, name='edit-task'),
    path('task/add', views.add_task, name='add-task'),
    
    path('opportunity', views.list_opportunity, name='list-opportunity'),
    path('opportunity/<int:id>/edit', views.edit_opportunity, name='edit-opportunity'),
    path('opportunity/add', views.add_opportunity, name='add-opportunity'),
    
    path(f'{settings.AAD_CONFIG.django.auth_endpoints.prefix}/', include(msal_urls)),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),

]