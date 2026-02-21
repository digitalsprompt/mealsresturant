from django.shortcuts import get_object_or_404, render, redirect
from . forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import Profile
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            user = authenticate(username=user.username, password = form.cleaned_data['password'])
            if user:
                login(request, user)
                messages.success(request, 'Signup successful!')
                return redirect('login')
    else:
        form = SignupForm()
        messages.error(request, 'Signup failed. Please correct the errors below.')
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return  redirect ('login')

def profile_details(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'profile_details.html', {'profile': profile})

def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile_details')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'profile_update.html', context)




