from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm
import os
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            sender = form.cleaned_data['sender']
            receiver = ['friturestegt.kylling@gmail.com']
            print(title, content, sender, receiver)
            send_mail(title, content, sender, receiver)
            return redirect('vault:home')
    else:
        form = ContactForm()
    return render(request, 'vault/contact.html', {'form':form})

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            tankolator = float(form.cleaned_data['tank_size'])*420
            hardnessolator = float(form.cleaned_data['water_hardness'])*420
            context = {
                'method': form.cleaned_data['method'],
                'tank_size': form.cleaned_data['tank_size'],
                'tankolator': tankolator,
                'water_type': form.cleaned_data['water_type'],
                'hardnessolator':hardnessolator,
                'water_hardness': form.cleaned_data['water_hardness'],
                'rhythm': form.cleaned_data['rhythm'],
                'conductivity': form.cleaned_data['conductivity'],
                }
            return render(request, 'vault/metode.html', context)
    else:
        form = NameForm()
    return render(request, 'vault/name.html', {'form': form})


def home(request):
    context = {}
    return render(request, 'vault/home.html', context)

def product(request):
    context = {}
    return render(request, 'vault/product.html', context)

def water_quality(request):
    context = {}
    return render(request, 'vault/quality.html', context)

def downloads(request):
    context = {}
    return render(request, 'vault/downloads.html', context)
