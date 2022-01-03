from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import Contact
from .forms import ContactForm



class ContactCreateView(LoginRequiredMixin, FormView):
    form_class = ContactForm
    template_name = 'crud/contact_form.html'

    def form_valid(self, form):
        contact = form.save(commit=False)
        contact.user = self.request.user
        contact.save()
        return redirect('contact:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Contact Create Form',
            'button': 'Create'
        })
        return context

class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'crud/contact_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Contact Update Form',
            'button': 'Update'
        })
        return context


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = 'crud/contact_confirm_delete.html'
    success_url = reverse_lazy('contact:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Contact Delete',
        })
        return context


class ContactListView(ListView):
    model = Contact
    template_name = 'crud/contact_list.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Contact.objects.filter(user=self.request.user)
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Contact List'
        })
        return context


