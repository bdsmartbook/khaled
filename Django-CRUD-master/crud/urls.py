from django.urls import path
from . import views


app_name = 'contact'
urlpatterns = [
    path('contact/create/', views.ContactCreateView.as_view(), name='create'),
    path('contact/update/<int:pk>/', views.ContactUpdateView.as_view(), name='update'),
    path('contact/delete/<int:pk>/', views.ContactDeleteView.as_view(), name='delete'),
    path('', views.ContactListView.as_view(), name='list'),
]
