from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from .models import Contacts
from .forms import ContactForm, ContactUpdateForm

# Create your views here.

# View to add Contact details


class ContactCreateView(TemplateView):

    template_name = "createcontact.html"
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def post(self, request):
        print(request.POST, '***********')
        form = self.form_class(request.POST, request.FILES)
        print(form, '-----------------')
        if form.is_valid():
            print(form.cleaned_data)
            Contacts.objects.create(**form.cleaned_data)
            print("contact created")
            return redirect("contact-list")


# To list the contact details
class ContactListView(TemplateView):

    model = Contacts
    template_name = "contactlist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contacts.objects.all()

        return context


# To Get the details of contact

class ContactDetailsView(TemplateView):

    model = Contacts
    template_name = "contactdetail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_id"] = Contacts.objects.get(id=kwargs['id'])
        return context


# To update a Contact

class ContactUpdateView(TemplateView):

    template_name = "updatecontact.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        contact = Contacts.objects.get(id=kwargs['id'])
        form = ContactUpdateForm(instance=contact)
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        instance = Contacts.objects.get(id=kwargs['id'])
        form = ContactUpdateForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('contact-list')
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


# To delete a Contact_id from record
def delete(request, **kwargs):
    cont_id = kwargs.get("id")
    contact = Contacts.objects.get(id=cont_id)
    contact.delete()
    return redirect("contact-list")
