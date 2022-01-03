from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from .forms import UserCreateForm



class UserCreateView(FormView):
    form_class = UserCreateForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        form.save()
        return redirect('login')


class UserProfileView(TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Profile',
        })
        return context