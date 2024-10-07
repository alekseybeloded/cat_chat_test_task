from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from cat.models import Cat


@login_required
def home_view(request):
    users = User.objects.exclude(id=request.user.id)
    cats = Cat.objects.filter(user=request.user)
    return render(request, 'home.html', {'cats': cats, 'users': users})


@login_required
def add_cat_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        breed = request.POST['breed']
        hairiness = request.POST['hairiness']
        Cat.objects.create(name=name, age=age, breed=breed, hairiness=hairiness, user=request.user)
        return redirect('home')
    return render(request, 'add_cat.html')


@login_required
def edit_cat_view(request, cat_id):
    cat = get_object_or_404(Cat, id=cat_id, user=request.user)
    if request.method == 'POST':
        cat.name = request.POST['name']
        cat.age = request.POST['age']
        cat.breed = request.POST['breed']
        cat.hairness = request.POST['hairiness']
        cat.save()
        return redirect('home')
    return render(request, 'edit_cat.html', {'cat': cat})


@login_required
def delete_cat_view(request, cat_id):
    cat = get_object_or_404(Cat, id=cat_id, user=request.user)
    if request.method == 'POST':
        cat.delete()
        return redirect('home')
    return render(request, 'delete_cat.html', {'cat': cat})


@login_required
def chat_with_user_view(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    return render(request, 'chat_with_other_user.html', {'other_user': other_user})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Неправильное имя пользователя или пароль.')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
