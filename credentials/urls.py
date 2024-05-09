from django.urls import path
from . import views
app_name='movie_app1' #namespace
urlpatterns = [

    path('register',views.register,name='register'),
    # path('login',views.login,name='login'),



]
