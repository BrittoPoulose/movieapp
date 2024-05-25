from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .models import Movie, Admin, registration,Review,Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from .forms import MovieForm
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import re
def index(request):
    category = Category.objects.all()
    movie = Movie.objects.filter(status='a')
    context={'category':category,'movies':movie}
    return render(request, 'index.html', context)
def admin_login(request):
    message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        admins = Admin.objects.all().values('username', 'password')  
        for admin in admins:
            if admin["username"] == username and admin["password"] == password:
                # request.session['user_id'] = admin["id"]
                return redirect('movie_app:mainadmin')
        message = "Invalid login"
    return render(request, 'adminlogin.html', {'message': message})
def mainadmin(request):
    return render(request, 'mainadmin.html')
def deleteuser(request):
    if request.method == 'POST':
        user_id = request.POST.get('delete')
        # print(movie_id
            # movie = get_object_or_404(Movie, id=movie_id)
        movie = get_object_or_404(registration, id=user_id)
        movie.status = "r"
        movie.save()
        return redirect('movie_app:adminpage')
    user=registration.objects.filter(status='a')
    return render(request, 'deleteuser.html',{'user':user})
def viewuser(request):
    user = registration.objects.filter(status='a')

    return render(request, 'viewuser.html',{'user':user})
def category_result(request,item_id):
    movie = Movie.objects.filter(category=item_id)
    return render(request, 'category_result.html', {'movies': movie})
def trailer(request):
    
    movie = Movie.objects.filter(status='a')
    return render(request, 'trailer.html', {'movies': movie})
def message(request,message):
    
    # movie = Movie.objects.filter(status='a')
    return render(request, 'messageuserlogin.html', {'message': message})
def messageregister(request):
    
    # movie = Movie.objects.filter(status='a')
    return render(request, 'messageregister.html')
def commingsoon(request):
    movie = Movie.objects.filter(theater='CS')
    return render(request, 'movie_status.html', {'movies': movie})
def out_of_theater(request):
    
    movie = Movie.objects.filter(theater='OT')
    return render(request, 'movie_status.html', {'movies': movie})
def intheater(request):
    
    movie = Movie.objects.filter(theater='IT')
    return render(request, 'movie_status.html', {'movies': movie})
def reviews(request):
    if request.method == 'POST':
        if 'review' in request.POST:
            movie_id = request.POST.get('review')
            return redirect('movie_app:reviews2', movie_id=movie_id)
        
    movie = Movie.objects.filter(status='a')

    
    return render(request, 'reviews.html', {'movies': movie})
def reviews2(request,movie_id):
    reviews = Review.objects.filter(m_id=movie_id)
    
    return render(request, 'reviews2.html', {'reviews': reviews})
def delete_category(request):
    if request.method == 'POST':
    
            
        cat_id = request.POST.get('delete_category')
        # print(movie_id)

            # movie = get_object_or_404(Movie, id=movie_id)
        category = get_object_or_404(Category, id=cat_id)
        category.status = "r"
        category.save()
        return redirect('movie_app:adminpage')
    
    category = Category.objects.filter(status='a')
    return render(request, 'delete_category.html', {'movies': category})
def add_category(request):
    if request.method == 'POST':
        if 'category' in request.POST:
            category = request.POST.get('category')
            category1 = Category(category=category)
            category1.save()
            return redirect('movie_app:adminpage')
        
    movies = Movie.objects.filter(status='a')

    return render(request, 'add_category.html')
def admin(request):
    return render(request, 'admin.html')
def delete(request):
    if request.method == 'POST':
        movie_id = request.POST.get('delete')
        # print(movie_id
            # movie = get_object_or_404(Movie, id=movie_id)
        movie = get_object_or_404(Movie, id=movie_id)
        movie.status = "r"
        movie.save()
        return redirect('movie_app:adminpage')

    movies = Movie.objects.filter(status='a')
    return render(request, 'delete.html', {'movies': movies})

def update(request):
    if request.method == 'POST':
        if 'update' in request.POST:
            movie_id = request.POST.get('update')
            return redirect('movie_app:update2', movie_id=movie_id)
        
    movies = Movie.objects.filter(status='a')

    return render(request, 'update.html', {'movies': movies})
def update2(request,movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        # Retrieve updated data from the POST request
        movie.name = request.POST.get('name')
        movie.actor = request.POST.get('actor')
        movie.description = request.POST.get('description')
        movie.theater = request.POST.get('theater')

        # Handle file upload for poster
        if 'poster' in request.FILES:
            poster = request.FILES['poster']
            fs = FileSystemStorage()
            filename = fs.save(poster.name, poster)
            movie.poster = fs.url(filename)
        # Save the updated instance to the database
        movie.save()
        # Redirect to a success page or return a response
        # This prevents the browser from resubmitting the form if the user refreshes the page
        return redirect('movie_app:movie_list')  # Replace 'movie_list' with your actual URL

    # If the request method is not POST, render the update form with the existing movie object
    return render(request, 'update2.html', {'movie': movie})
def create_admin(request):
    username = 'admin'
    password = '1234'
    
    if not Admin.objects.filter(username=username).exists():
        admin = Admin(username=username, password=password)
        admin.save()
        return render(request, 'admin_created.html', {'admin': admin})
    else:
        return render(request, 'admin_exists.html')

def registrations(request):
    message=""
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if registration.objects.filter(username=username).exists():
            message='Username already exists.'
        elif registration.objects.filter(email=email).exists():
            message='Email already exists.'
        else:
            user = registration(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            messages.success(request, 'Registration successful.')
            return redirect('movie_app:messageregister')
    return render(request,'registration.html' ,{'message': message})

def login(request):
    message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        admins = registration.objects.all().values('id','username', 'password','status')  
        for admin in admins:
            if admin["username"] == username and admin["password"] == password and admin['status']=='a':
                request.session['user_id'] = admin["id"]
                message1="login"
                return redirect('movie_app:message',message=message1)
        message = "Invalid login"
    return render(request, 'login.html', {'message': message})

def add_movie(request):
    categories = Category.objects.filter(status='a')

    if request.method == 'POST':
        name = request.POST.get('name')
        actor = request.POST.get('actor')
        description = request.POST.get('description')
        theater = request.POST.get('theater')
        category = request.POST.get('category')
        rdate = request.POST.get('rdate')
        trailer_link = request.POST.get('trailer_link')

        pattern = r'^.*(?:youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=)([^#\&\?]*).*'
        match = re.match(pattern, trailer_link)
        trailer1=match.group(1)
        if 'poster' in request.FILES:
            poster = request.FILES['poster']
        else:
            poster = None
        # Check if 'user_id' exists in the session
        if 'user_id' in request.session:
            user_id = request.session['user_id']
            new_movie = Movie(name=name, actor=actor, description=description, poster=poster, ruserid=user_id,theater=theater,category=category,rdate=rdate,trailer_link=trailer1)
            new_movie.save()
            return redirect('movie_app:movie_list')
        else:
            # Redirect to login page if user is not logged in
            return redirect('movie_app:login')
    else:
        return render(request, 'add_movie.html',{'category': categories})

def add_review(request):
    if request.method == 'POST':
        if 'm_id' in request.POST:
            movie_id = request.POST.get('m_id')
            return redirect('movie_app:add_review2', movie_id=movie_id)
        
    movies = Movie.objects.filter(status='a')

    return render(request, 'add_review.html', {'movies': movies})
def add_review2(request,movie_id):
    # movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        # Retrieve updated data from the POST request
        review = request.POST.get('review')
        rating = request.POST.get('rating')
        reviews = Review(m_id=movie_id, review1=review,rating=rating)
        reviews.save()
        return redirect('movie_app:adminpage')

      
    return render(request, 'add_review2.html')
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})
def search_movies(request):
    query = request.GET.get('q')
    movies = []

    if query:
        movies = Movie.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'movies': movies, 'query': query})
