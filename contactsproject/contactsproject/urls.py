"""
URL configuration for contactsproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from contactapp import views
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ContactCreateView.as_view(),name='contact-create'),
    path('mycontacts',views.ContactListView.as_view(),name ="contact-list"),
    path('details/<int:id>',views.ContactDetailsView.as_view(),name ="contact-detail"),
    path('mycontacts/update/<int:id>',views.ContactUpdateView.as_view(),name ="contact-update"),
    path('mycontacts/<int:id>/delete',views.ContactDetailsView.as_view(),name="delete"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
