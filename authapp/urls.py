from django.contrib import admin
from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('signup/',views.signup),
    path('home/',views.home,name='home'),
    path('logout/',views.user_logout),

]
