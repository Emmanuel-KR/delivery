from pdb import post_mortem
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.


def home(request):
    return render(request, 'base/home.html')


@login_required()
def customerPage(request):
    return render(request, 'base/home.html')


@login_required()
def courierPage(request):
    return render(request, 'base/home.html')


def signUp(request):
    form = forms.SignUpForm
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email').lower()

            user = form.save(commit=False)
            user.username = email
            user.save()

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')

    context = {'form': form}
    return render(request, 'base/sign_up.html', context)
