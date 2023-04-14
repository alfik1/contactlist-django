from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from .models import Contacts
from .forms import ContactForm,ContactUpdateForm

# Create your views here.

#View to add Contact details
class ContactCreateView(View):
    
    def get(self, request):
        form = ContactForm()
        return render(request,"createcontact.html",{'form': form })
    
    def post(self, request):
        print(request.POST,'***********')
        form =  ContactForm(request.POST, request.FILES)
        print(form,'-----------------')
        if form.is_valid():
            print(form.cleaned_data)
            Contacts.objects.create(**form.cleaned_data)
            print("contact created") 
            return redirect("contact-list")   
        

#To list the contact details
class ContactListView(TemplateView):
    template_name = "contactlist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contacts.objects.all()
        
        return context
    

#To Get the details of contact

class ContactDetailsView(TemplateView):

    def get(self,request,id):
        
        contact=Contacts.objects.get(id=id) #we're getting a single instance of Contact from Contacts by passing an ID value.
        return render(request, "contactdetail.html",{'contact':contact})


#To update a Contact

class ContactUpdateView(TemplateView):
    


    def get(self,request,*args,**kwargs):
        id= kwargs.get("id")
        update = Contacts.objects.get(id = id)
        form = ContactUpdateForm(instance = update)
        return render(request,"updatecontact.html",{'form':form})



def remove_contact(request, **kwargs):
    cont_id=kwargs.get("id")
    Contacts.objects.get(id=cont_id).delete()
    return redirect("contact-list")