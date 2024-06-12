from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Flan, ContactForm
from .forms import ContactFormModelForm, CustomUserCreationForm

# Create your views here.
def indice(request):
    flanes = Flan.objects.all()
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        'flanes': flanes,
        'flanes_publicos' : flanes_publicos
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        'flanes_privados' : flanes_privados
    }
    return render(request, 'welcome.html', context)

def base(request):
    return render(request, 'base.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            
            return HttpResponseRedirect('/exito/')
    else:
        form = ContactFormModelForm()
        
    return render(request, 'contactus.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')

def login(request):
    return render(request, 'login.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('/bienvenido/')
        else:
            data['form'] = user_creation_form

    return render(request, 'registro.html', data)
'''
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('/bienvenido/')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)
    
'''

def logout(request):
    return HttpResponseRedirect('/')