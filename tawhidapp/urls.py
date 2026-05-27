from django.urls import path
from .views import *

urlpatterns = [

   path('register/', registerPage, name='register'),
   path('', loginPage, name='login'),
   path('logout/', logoutPage, name='logout'),
   path('home/', homePage, name='home'),
   path('add-cash/', addCashPage, name='addCash'),
   path('expend-cash/', expendCashPage, name='expendCash'),
   path('profile/', profilePage, name='profile'),

 
]
