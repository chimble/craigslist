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
from craigapp.models import Craig, Ad


def index(request):
    return render(request, 'index.html')


def profile_view(request):
    return render(request, 'profile.html')


def car_view(request):
    return render(request, 'cars.html')


def create_ad(request):
    if request.method == "POST":
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user_id = request.user.id
            ad.save()
            #login(request, ad)
            return HttpResponseRedirect('/craigapp/accounts/profile')
    else:
        form = AdForm()
        return render(request, 'create_ad.html', {'form': form})

def ad_listing(request):
    ads = models.Ad.objects.all()
    return render(request, 'ad_listing.html', {'ads': ads})

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
