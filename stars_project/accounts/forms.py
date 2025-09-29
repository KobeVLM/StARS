from django import forms
from .models import Blog, Artwork, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter first name'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter last name'}), required=False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Blog title'}),
            'description': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Short description'}),
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter content'})
        }
    
#To implement images daw kay need ug ImageField and then i-modify ang settings.py to include media
class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Artwork title'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Short description'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Write a comment...'})
        }