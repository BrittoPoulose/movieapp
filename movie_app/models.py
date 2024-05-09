from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
#britto changes
class Movie(models.Model):
    # name = models.CharField(max_length=255)
    name = models.CharField(max_length=255, default="Untitled Movie")

    actor = models.CharField(max_length=255, default="Unknown")

    # actor = models.CharField(max_length=255)
    description = models.TextField(default="No description available")


    # description = models.TextField()
    # poster = models.ImageField(upload_to='posters/')

    poster = models.ImageField(upload_to='posters/', default="default_poster.jpg")

# class Movie(models.Model):
#     pass
    # title = models.CharField(max_length=100)
    # poster = models.ImageField(upload_to='posters/')
    # description = models.TextField()
    # release_date = models.DateField()
    # actors = models.CharField(max_length=255, default='Unknown')
    # actors = models.CharField(max_length=200)
    # category = models.CharField(max_length=50)
    # trailer_link = models.URLField()
    # added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    rating = models.IntegerField()
class UserCredentials(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    class Meta:
        db_table = 'movie1'

class Admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

# from django.db import models


# class Movie(models.Model):
#     title = models.CharField(max_length=100)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     description = models.TextField()
#     img = models.ImageField(upload_to='gallery')
#     # Add more fields as needed
#
#     def __str__(self):
#         return self.title

