from django.shortcuts import render,redirect
from .models import Contact

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        return redirect('home')
    return render(request, 'contact.html')

def home(request):
    return render(request, 'portfolio.html')


def about(request):
    return render(request, 'about.html')


def skills(request):
    return render(request, 'skills.html')


def education(request):
    return render(request, 'education.html')


def project(request):
    return render(request, 'project.html')


def certificate(request):
    return render(request, 'certificate.html')