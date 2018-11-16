from django.urls import path

from . import views


app_name = 'Thunder'
urlpatterns = [
                  path('home/', views.home, name='home'),

]