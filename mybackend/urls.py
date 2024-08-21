# mybackend/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views  # Ensure this import is present
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.home, name='home'),
    # Route to home view
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
