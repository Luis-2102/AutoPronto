from django.shortcuts import render
from django.views.generic.base import TemplateView
from email.mime.text import MIMEText
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import smtplib
from .models import Servicio, Entregas, Testimonios, Preguntas, Ventajas, Galeria


class home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Servicio.objects.all()
        context['entregas'] = Entregas.objects.all()
        context['testimonios'] = Testimonios.objects.all()
        context['preguntas'] = Preguntas.objects.all()
        return context


def contact(request):
    return render(request, 'contact.html')

def cotizacion(request):
    return render(request, 'cotizacion.html')

def pricing(request):
    return render(request, 'pricing.html')


def service_details(request):
    galeria = Galeria.objects.all()
    return render(request, 'service-details.html', {'galeria': galeria})

def about(request):
    testimonios = Testimonios.objects.all()
    preguntas = Preguntas.objects.all()
    
    services = Servicio.objects.all()
    return render(request, 'about.html', {'testimonios': testimonios, 'preguntas':preguntas, 'services': services})

def featured_services(request):
    services = Servicio.objects.all()
    entregas = Entregas.objects.all()
    testimonios = Testimonios.objects.all()
    ventajas = Ventajas.objects.all()
    return render(request, 'services.html', {'entregas': entregas, 'services': services, 'testimonios': testimonios, 'ventajas': ventajas})
   