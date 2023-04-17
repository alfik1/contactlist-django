from django import forms
from .models import Contacts


# form for Contact adding

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields = ['name', 'gender', 'email', 'phone', 'image']
    
        widgets = {
            "name" :forms.TextInput(attrs={"class":"form-control border border-dark","placeholder":"enter name"}),
            "email": forms.EmailInput(attrs={"class": " form-control border border-dark", "placeholder": "enter email"}),
            "phone" :forms.NumberInput(attrs={"class": " form-control border border-dark", "placeholder": "enter phone number"}),
            "images":forms.FileInput(attrs={"class":"form-select mt-2"})
        }

#form to update the contact details
class ContactUpdateForm(forms.ModelForm):
        
    class Meta:
        model = Contacts
        fields = "__all__"

        widgets = {
            "name" :forms.TextInput(attrs={"class":"form-control border border-dark","placeholder":"enter name"}),
            "email": forms.EmailInput(attrs={"class": " form-control border border-dark", "placeholder": "enter email"}),
            "phone" :forms.NumberInput(attrs={"class": " form-control border border-dark", "placeholder": "enter email"}),
            "images":forms.FileInput(attrs={"class":"form-select mt-2"})
        }