from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from crud import views as crud_views


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/logged_in.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile', views.UserProfileView.as_view(), name='profile'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
    path('', crud_views.ContactListView.as_view(), name='password_change_done'),
    path('accounts/register/', views.UserCreateView.as_view(), name='register'),
]