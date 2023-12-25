from django.urls import path
from .import views

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('login/',views.user_login, name='login'),
    path('profile/',views.profile, name='profile'),
    path('change_pass/',views.change_pass, name='change_pass'),
    path('change_pass2/',views.change_pass2, name='change_pass2'),
    path('logout/',views.user_logout, name='logout'),
    path('',views.home),
]
