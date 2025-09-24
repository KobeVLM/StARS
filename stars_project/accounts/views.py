from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse

def login_view(request):
    """Handle user login"""
    # Don't redirect if already authenticated, just show the login page with a message
    if request.user.is_authenticated:
        messages.info(request, f'You are already logged in as {request.user.username}.')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            # Just stay on login page after successful login for now
            return render(request, 'accounts/login.html')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'accounts/login.html')

def register_view(request):
    """Handle user registration"""
    # Don't redirect if already authenticated, just show a message
    if request.user.is_authenticated:
        messages.info(request, f'You are already logged in as {request.user.username}.')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Debug: Print received data
        print(f"DEBUG: Registration attempt - Username: {username}, Email: {email}")
        
        # Validation
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'accounts/register.html')
        
        if len(password1) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
            return render(request, 'accounts/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'accounts/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'accounts/register.html')
        
        # Create new user
        try:
            print(f"DEBUG: About to create user...")
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                first_name=first_name,
                last_name=last_name
            )
            print(f"DEBUG: User created successfully - ID: {user.id}, Username: {user.username}")
            
            # Verify user was saved
            saved_user = User.objects.get(id=user.id)
            print(f"DEBUG: User verification - Found user: {saved_user.username}")
            
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('accounts:login')
        except Exception as e:
            print(f"DEBUG: Error creating user: {e}")
            messages.error(request, 'Error creating account. Please try again.')
    
    return render(request, 'accounts/register.html')

def logout_view(request):
    """Handle user logout"""
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
    return redirect('accounts:login')

