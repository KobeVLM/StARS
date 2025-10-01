from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

#For blog posts; Blogs are associated with a user
class Blog(models.Model):
    blogId = models.AutoField(primary_key=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#For artworks; Artworks are associated with a user
class Artwork(models.Model):
    artId = models.AutoField(primary_key=True, unique=True)
    artist = models.ForeignKey(User, on_delete=models.CASCADE, related_name="artworks")
    title = models.CharField(max_length=50)
    description = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#For comments; Comments are associated with a user, blog post (can be empty), and artwork (can be empty)
class Comment(models.Model):
    commentId = models.AutoField(primary_key=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True, related_name="comments")
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, null=True, blank=True, related_name="comments")

    def __str__(self):
        return f"Comment by {self.author.username}"

#For tags; Tags are associated with blogs or artwork/s
class Tag(models.Model):
    tagId = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=30, unique=True)
    blogs = models.ManyToManyField(Blog, blank=True, related_name="tags")
    artworks = models.ManyToManyField(Artwork, blank=True, related_name="tags")

    def __str__(self):
        return self.name

#For favorites or bookmarks; Favorites are associated with a blog or artwork/s
class Favorite(models.Model):
    favoriteId = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True, related_name="favorites")
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, null=True, blank=True, related_name="favorites")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Favorite by {self.user.username}"