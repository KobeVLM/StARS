from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Import forms and models from the accounts app
from accounts.forms import RegisterForm, LoginForm, BlogForm, ArtworkForm, CommentForm
from accounts.models import Blog, Artwork, Comment

# Register
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('accounts:login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

# Login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('accounts:landing')  # Redirect to Landing page
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('accounts:login')

# Blogs
@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  # your model uses 'author', not 'user'
            blog.save()
            return redirect('accounts:login')  # Temporary redirect until home page exists
    else:
        form = BlogForm()
    return render(request, 'accounts/blog_form.html', {'form': form})

# Artworks
@login_required
def upload_artwork(request):
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.artist = request.user  # your model uses 'artist', not 'user'
            artwork.save()
            return redirect('accounts:login')  # Temporary redirect until home page exists
    else:
        form = ArtworkForm()
    return render(request, 'accounts/artwork_form.html', {'form': form})

# Comments
@login_required
def add_comment(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user  # your model uses 'author', not 'user'
            comment.blog = blog
            comment.save()
            return redirect('blog_detail', blog_id=blog.id)
    else:
        form = CommentForm()
    return render(request, 'accounts/comment_form.html', {'form': form, 'blog': blog})

# Landing Page
@login_required
def landing_page(request):
    # Get user statistics for the dashboard
    user_artworks = Artwork.objects.filter(artist=request.user)
    user_blogs = Blog.objects.filter(author=request.user)
    
    # Calculate user level and XP (example logic)
    total_content = user_artworks.count() + user_blogs.count()
    level = min(total_content // 5 + 1, 10)  # Level up every 5 pieces, max level 10
    xp = total_content * 100  # 100 XP per content piece
    
    context = {
        'level': level,
        'xp': xp,
        'artwork_created': user_artworks.count(),
        'ocs_drawn': user_artworks.count(),  # For now, same as artwork count
        'blogs_written': user_blogs.count(),
    }
    return render(request, 'accounts/landingpage.html', context)