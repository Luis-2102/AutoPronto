from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', home.as_view(), name="home"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cotizacion/', views.cotizacion, name='cotizacion'), 
    path('pricing/', views.pricing, name='pricing'),
    path('service-details/', views.service_details, name='service_details'),
    path('services/', views.featured_services, name='services'),  
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

