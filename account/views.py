from django.shortcuts import render
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from .forms import RegistrationForm
from .forms import *
from django.shortcuts import redirect
from django.template.loader import render_to_string


from .models import UserBase
   
def account_register(request):
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():            
            registerForm.save()
            return HttpResponseRedirect(reverse('account:login'))
    else: 
        registerForm = RegistrationForm()
    return render(request, 'account/registration/register.html', {'form':registerForm}) 

def login(request):
    if request.method == 'POST':
        registerForm = UserLoginForm(request.POST)
        if registerForm.is_valid():            
            registerForm.save()
            return render(request, 'store/home.html')
    else: 
        registerForm = RegistrationForm()
    return render(request, 'account/registration/login.html', {'form':registerForm}) 
