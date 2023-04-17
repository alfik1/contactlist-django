from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from .models import Contacts
from .forms import ContactForm, ContactUpdateForm

# Create your views here.

# View to add Contact details


class ContactCreateView(View):

    def get(self, request):
        form = ContactForm()
        return render(request, "createcontact.html", {'form': form})

    def post(self, request):
        print(request.POST, '***********')
        form = ContactForm(request.POST, request.FILES)
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

    def get(self, request, id):

        # we're getting a single instance of Contact from Contacts by passing an ID value.
        contact = Contacts.objects.get(id=id)
        return render(request, "contactdetail.html", {'contact': contact})
    
    def delete(request, **kwargs):
        cont_id = kwargs.get("id")
        print(cont_id,"*************")
        Contacts.objects.get(id=cont_id).delete()
        print(cont_id,"################")

        return redirect("contact-list")


# To update a Contact

class ContactUpdateView(TemplateView):

    template_name = "updatecontact.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        contact = Contacts.objects.get(id=kwargs['id'])
        form = ContactForm(instance=contact)
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        instance = Contacts.objects.get(id=kwargs['id'])
        form = ContactForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("contact-list")
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


