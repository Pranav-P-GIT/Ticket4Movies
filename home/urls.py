from django.urls import path
from home import views

urlpatterns = [
    path('', views.index,name='homepage'),
    path('login', views.login,name='loginpage'),
    path('register', views.register,name='registerpage'),
    path('movie', views.movie,name='moviepage'),
    path('thankyou', views.thankyou,name='thankyoupage'),    
    path('logout', views.logout,name='logoutpage'),    
    path('booking', views.booking,name='bookingpage'),    
    path('gallery', views.gallery,name='gallerypage'),    

]