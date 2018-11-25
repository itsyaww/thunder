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
    #Register
    path('register/', views.register, name='register'),
    #Upload Image
    path('profile/<int:member_id>/uploadimage/', views.upload_image, name='register'),
    #Profile
    path('profile/<int:member_id>', views.profile, name='profile'),
    #Display list of people with common hobbies
    path('matchlist/', views.matchlist, name='matchlist'),
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