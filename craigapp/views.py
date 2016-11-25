from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from craigapp.forms import *
from craigapp import models
from django.middleware import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth


def index(request):
    return render(request, 'index.html')


def profile_view(request):
    return render(request, 'profile.html')


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
            login(request, user)
            return HttpResponseRedirect('/craigapp/accounts/profile')
    else:
        form = UserForm()
        return render(request, 'create_user.html', {'form': form})
