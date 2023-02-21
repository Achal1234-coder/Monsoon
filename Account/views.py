from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .forms import FormRegistration, FormLogIn
from.models import User
from django.contrib import messages
from .utils import *
from django.contrib.auth import login, authenticate
from .models import User


class Registration(generic.FormView):
    form_class = FormRegistration
    template_name = "Account/register.html"

    def get(self, request) -> HttpResponse:
        return render(request, self.template_name, {'form': self.form_class})
    
    def post(self, request) -> HttpResponse:

        form = FormRegistration(request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data['name'], email=form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('/login')
        
        messages.error(request, form.errors)
        return render(request, self.template_name, {'form': self.form_class})

        
class LogIn(generic.FormView):
    form_class = FormLogIn
    template_name = 'Account/login.html'

    def get(self, request) -> HttpResponse:
        return render(request, self.template_name, {'form': self.form_class})
    
    def post(self, request):

        form = FormLogIn(request.POST)
        if form.is_valid():
            email = User.objects.get(email=request.POST['email'])
            user = authenticate(request, email=email, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                respone = redirect("/home")
                respone.set_cookie('email', email)
                respone.set_cookie('login_status', True)
                return respone
                
            messages.info(request, 'User not authorize to login')
        else:
            messages.info(request, form.errors)
        
        return render(request, self.template_name, {'form': self.form_class})
    

class LogOut(generic.FormView):
    def get(self, request):
        response = redirect('/')
        response.delete_cookie('email')
        response.delete_cookie('login_status')
        return response
    


class Home(generic.FormView):
    template_name = 'Account/home.html'

    def get(self, request):
        try:
            email = request.COOKIES['email']
        except KeyError:
            return redirect('/login')
        user = User.objects.get(email=email)
        name = user.username
        return render(request, self.template_name, {'name': name})

                    
