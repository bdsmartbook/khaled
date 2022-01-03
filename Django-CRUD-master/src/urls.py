import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path(str(os.environ.get('ADMIN_URL', 'admin/')), admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('crud.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
