from django.urls import path

from thunderapp import views


app_name = 'thunderapp'
urlpatterns = [
                  path('home/', views.home, name='home'),

]