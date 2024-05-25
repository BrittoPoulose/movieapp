from django.urls import path
from . import views

app_name = 'movie_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('create_admin/', views.create_admin, name='create_admin'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('search/', views.search_movies, name='search_movies'),
    path('movie_list/', views.movie_list, name='movie_list'),
    path('registrations/', views.registrations, name='registrations'),
    path('adminpage/', views.admin, name='adminpage'),
    path('update/', views.update, name='update'),
    path('update2/<int:movie_id>/', views.update2, name='update2'),
    path('delete/', views.delete, name='delete'),
    path('add_review/', views.add_review, name='add_review'),
    path('add_review2/<int:movie_id>/', views.add_review2, name='add_review2'),
    path('add_category/', views.add_category, name='add_category'),
    path('delete_category/', views.delete_category, name='delete_category'),
    path('reviews/', views.reviews, name='reviews'),
    path('reviews2/<int:movie_id>/', views.reviews2, name='reviews2'),
    path('commingsoon/', views.commingsoon, name='commingsoon'),
    path('intheater/', views.intheater, name='intheater'),
    path('out_of_theater/', views.out_of_theater, name='out_of_theater'),
    path('category_result/<int:item_id>/', views.category_result, name='category_result'),
    path('trailer/', views.trailer, name='trailer'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('mainadmin/', views.mainadmin, name='mainadmin'),
    path('viewuser/', views.viewuser, name='viewuser'),
    path('deleteuser/', views.deleteuser, name='deleteuser'),
    path('message/<message>/', views.message, name='message'),
    path('messageregister/', views.messageregister, name='messageregister'),

]
