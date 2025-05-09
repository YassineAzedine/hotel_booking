# contact/views.py
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Enregistrement du message dans la base de données
        ContactMessage.objects.create(name=name, email=email, message=message)

        # Message de succès
        messages.success(request, 'Votre message a été envoyé avec succès.')

        return HttpResponseRedirect(request.path_info)

    return render(request, 'contact/contact.html')