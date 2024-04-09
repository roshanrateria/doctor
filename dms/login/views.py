from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import User

def index(request):
    return render(request, 'login/index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('type')
        new_user = User(username=username, password=password, user_type=user_type)
        new_user.save()
        return redirect('login')
    return render(request, 'login/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password).first()
        if user:
            request.session['user_id'] = user.id
            return render(request, 'login/userpage.html', {'user': user})
    return render(request, 'login/login.html')

@login_required
def userpage(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        return render(request, 'login/userpage.html', {'user': user})
    else:
        return redirect('login')

def signout(request):
    del request.session['user_id']
    return redirect('login')