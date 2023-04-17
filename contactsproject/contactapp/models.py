from django.db import models

# Create your models here.

# model to add contact details


class Contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    gender_choices = {
        ('male', 'Male'),
        ('female', 'Female')
    }
    gender = models.CharField(choices=gender_choices, max_length=10, null=True, blank=True)
    image = models.ImageField(upload_to='media', blank=True, null=True)


def __str__(self):
    return self.contact_name
