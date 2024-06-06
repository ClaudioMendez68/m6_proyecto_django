from django.shortcuts import render, HttpResponseRedirect
from .models import Flan, ContactForm
from web.forms import ContactFormModelForm

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

def logout(request):
    return render(request, 'logout.html')