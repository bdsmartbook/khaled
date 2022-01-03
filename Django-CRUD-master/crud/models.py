from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact:list')
    
    def get_update_url(self):
        return reverse('contact:update', kwargs={
            'pk': self.id 
        })

    def get_delete_url(self):
        return reverse('contact:delete', kwargs= {
            'pk': self.id
        })
