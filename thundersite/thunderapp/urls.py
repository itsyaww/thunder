from django.urls import path

from thunderapp import views


app_name = 'thunderapp'
urlpatterns = [
    #Default page
    path('', views.index, name='index'),
    #Login page
    path('login/', views.index, name='login'),
    #Signup Page
    path('signup/', views.signup, name='signup'),
    #Profile
    path('profile/<int:member_id>', views.profile, name='profile'),
    #Display list of people with common hobbies
    path('matchlist/', views.matchlist, name='matchlist'),
    path('register/', views.register, name='register'),
    path('messages/', views.messages, name='messages'),
    path('profile/<int:member_id>/uploadimage/', views.upload_image, name='register'),

]