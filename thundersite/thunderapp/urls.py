from django.urls import path

from thunderapp import views
from django.contrib.auth import views as auth_views


app_name = 'thunderapp'
urlpatterns = [
    #Default page
    path('', views.login, name='index'),
    #Login page
    path('login/', views.login, name='login'),
    #Signup Page
    path('signup/', views.signup, name='signup'),
    #Register
    path('register/', views.register, name='register'),
    #Upload Image
    path('profile/<int:member_id>/uploadimage/', views.upload_image, name='register'),
    path('profile/<int:member_id>/updateprofile/', views.update_profile_details, name='updateprofile'),
    path('profile/', views.profile, name='profile'),
    #Profile
    path('profile/<int:member_id>', views.get_friend_profile, name='friendprofile'),
    #Display list of people with common hobbies
    path('matchlist/<int:member_id>', views.matchlist, name='matchlist'),
    # messages page
    path('messages/', views.messages, name='messages'),
    # Ajax: check if user exists
    path('checkuser/', views.checkuser, name='checkuser'),
    # Ajax: post a new message
    path('postmessage/', views.post_message, name='postmessage'),
    # Ajax: delete a message
    path('erasemessage/', views.erase_message, name='erasemessage'),
    path('messages/', views.messages, name='messages'),


]