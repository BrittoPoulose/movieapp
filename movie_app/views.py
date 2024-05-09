from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import UserCredentials,Movie,Admin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import MovieForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import check_password
def index(request):
    obj=Movie.objects.all()
    return render(request,'index.html',{'result':obj})


# def search_results(request):
#     search_query = request.GET.get('search_field', '')
#     Here, 'search_query' will hold the value entered in the search field
#     You can then use this value to perform your search logic

#     For example, you might pass this query to a function that retrieves search results
#     results = perform_search_function(search_query)

#     For simplicity, we'll just pass the search query back to the template
#     return render(request, 'search_result.html', {'search_query': search_query})
from .models import UserCredentials
def create_admin(request):
    username = 'admin'
    password = '1234'
    
    # Check if an admin with the same username already exists
    if not Admin.objects.filter(username=username).exists():
        admin = Admin(username=username, password=password)
        admin.save()
        return render(request, 'admin_created.html', {'admin': admin})
    else:
        return render(request, 'admin_exists.html')

def login(request):
    message=""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        admins = Admin.objects.all().values('username', 'password')
        
        # admins = Admin.objects.filter(username=username)
        # admins2 = Admin.objects.filter(password=password)
        if admins[0]["username"]==username and admins[0]["password"]==password:
            message="success login"
            return render(request, 'add_movies.html')
        else:
            message="Invalid login"
            return render(request, 'login.html',{'message':message})



        # print(admins)
        # print(admins2)

    return render(request, 'login.html',{'message':message})


        # Retrieve the admin object based on the provided username
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
                # Redirect to the movie list page after saving the movie
            return redirect('movie_app:movie_list')  # Using the app namespace
    else:
        form = MovieForm()
    return render(request, 'movie_app/add_movie.html', {'form': form})

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_app/movie_list.html', {'movies': movies})
def search_movies(request):
    query = request.GET.get('q')
    movies = []
    movies1 = []
    movies2 = []
    movies3 = []


    if query:
        movies = Movie.objects.filter(name__icontains=query)
        # movies1 = Movie.objects.filter(actor__icontains=query)
        # movies2 = Movie.objects.filter(description__icontains=query)
        # movies3 = Movie.objects.filter(poster__icontains=query)


    return render(request, 'search_results.html', {'movies': movies, 'query': query})