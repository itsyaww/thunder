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
    path('profile/', views.profile, name='profile'),
    #Display list of people with common hobbies
    path('matchList/', views.matchList, name='matchList'),
]