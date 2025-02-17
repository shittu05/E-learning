from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegForm
from django.shortcuts import render, redirect
from django.shortcuts import render

from django.contrib.auth.models import auth
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm



# Create your models here.

def index(request):
    return render(request, 'index.html')


 # Ensure you import your User model

def register(request):
    if request.user.is_authenticated:
        return redirect("/learn/courses/")

    if request.method == 'POST':
        form = RegForm(request.POST)

        if form.is_valid():
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already taken')
                return redirect('/register/')

            else:
                form.save()
                user = authenticate(email=email,password = password)
                auth.login(request, user)  # Use login instead of auth.login
                messages.success(request, "Student account created successfully")
                return redirect('/login/')

        else:
            # Loop through form errors and add them to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
            return render(request, 'registration.html', {'form': form})

    else:
        form = RegForm()
        return render(request, 'registration.html', {'form': form})

    


def login(request):

    # if request.user.is_authenticated:
    #     return redirect('/login/')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            auth.login(request,user)
            messages.success(request, f'Welcome {username}')
            return redirect('/learn/courses/')
        else:
            messages.error(request, 'invalid login details')
            form = AuthenticationForm()
            return render(request,'login.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
    
    
 
def logout(request):
    request.session.clear()
    messages.info(request, "You have been logged out")
    return redirect('login')