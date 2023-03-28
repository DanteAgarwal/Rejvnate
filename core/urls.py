from django.urls import path 
from .views import home , login_register , contact , story , services ,services1,services2, services3 , services4 , services5, services6


urlpatterns = [
    path("",home,name="Home"),
    path("login/", login_register , name='Login'),
    path("contact/" , contact , name="Contact"),
    path("story/", story , name="Story"),
    path("services/", services , name="Services" ),
    path("Physiotherapy/", services1 , name="Services1" ),
    path("Naturopathy/", services2 , name="Services2" ),
    path("Beauty_spa/", services3 , name="Services3" ),
    path("Fitness/", services4 , name="Services4" ),
    path("Diet/", services5 , name="Services5" ),
    path("Yoga/", services6 , name="Services6" ),

    
    ]