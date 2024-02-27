from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from . import forms


def logout_user(request):
    """
    Function logging out the user
    """

    logout(request)
    return redirect('login')


def signup_page(request):
    """
    Function working on the signup 
    """

    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})
