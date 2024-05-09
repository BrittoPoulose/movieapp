from django.urls import path
from . import views

app_name = 'movie_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('create_admin/', views.create_admin, name='create_admin'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('search/', views.search_movies, name='search_movies'),
    path('movie_list/', views.movie_list, name='movie_list'),  # Updated this line
    path('search_movies/', views.search_movies, name='search_movies'),  # Updated this line

]
