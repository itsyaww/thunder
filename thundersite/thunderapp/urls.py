from django.urls import path

from thunderapp import views
from django.contrib.auth import views as auth_views


app_name = 'thunderapp'
urlpatterns = [
    #Default page
    path('', views.login, name='index'),
    #Login page
    path('login/', views.login, name='login'),
    # logout page
    path('logout/', views.logout, name='logout'),
    #Signup Page
    path('signup/', views.register, name='register'),
    #Register
    path('register/', views.register, name='register'),
    #Upload Image
    path('profile/<int:member_id>/uploadimage/', views.upload_image, name='register'),
    #Update Profiles
    path('profile/<int:member_id>/updateprofile/', views.update_profile_details, name='updateprofile'),
    #View list of profiles
    path('profiles/', views.list_of_members, name='profiles'),
    #Search profiles
    path('profiles/search/', views.search_members, name='searchmembers'),
    path('profiles/searchgender/', views.search_gender, name='search_gender'),

    path('profile/', views.profile, name='profile'),
    #Profile of a friend
    path('profile/<int:member_id>', views.get_friend_profile, name='friendprofile'),
    #Display list of people with common hobbies
    path('matchlist/', views.matchlist, name='matchlist'),
    # messages page
    path('messages/', views.messages, name='messages'),
    # getMessages Ajax
    path('getMessages/', views.getMessages, name='getMessages'),
    # Ajax: check if user exists
    path('checkuser/', views.checkuser, name='checkuser'),
    # Ajax: post a new message
    path('postmessage/', views.post_message, name='postmessage'),
    # Ajax: delete a message
    path('erasemessage/', views.erase_message, name='erasemessage'),


]