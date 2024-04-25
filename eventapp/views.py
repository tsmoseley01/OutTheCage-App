from django.shortcuts import render, redirect
from .models import Event
from .forms import RegistrationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
def faq(request):
    return render(request, 'faq.html')
def events(request):
    dict_event={
        'event':Event.objects.all()
    }
    return render(request, 'events.html',dict_event)
def registration(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    form=RegistrationForm()
    dict_form={
        'form':form

    }
    return render(request, 'registration.html', dict_form)
def contact(request):
    return render(request, 'contact.html')
