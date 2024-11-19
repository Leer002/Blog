from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


from .forms import UserRegisterForm

class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form, 'title': 'register here'})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is taken")
                return redirect('list')
            
            user_obj = form.save(commit=False)
            user_obj.set_password(password)  
            user_obj.save() 

            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('profile')
            
        return render(request, "users/register.html", {"form":form})


class UserLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form, 'title': 'log in'})
    
    def post(self, request):
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.error(request, "Username not found")
                return redirect('register')
            user_obj = authenticate(username = username, password = password)
            if user_obj:
                login(request, user_obj)
                return redirect('profile')
            messages.error(request, "Wrong Password")
            return redirect('login')
             
        except Exception as e:
            messages.error(request, " Somthing went wrong")
            return redirect('list')
    
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, "users/index.html")
    


