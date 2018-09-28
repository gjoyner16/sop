from django.contrib import auth
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm, ChangeUserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from sop.urls import *

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=raw_password)
            auth.login(request, user)
            return redirect('client_list')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def edit_user(request):
    if request.method == 'POST':
        form = ChangeUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ChangeUserForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/user.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user')
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
        args = {'form': form}
        return render(request, 'password.html', args)
