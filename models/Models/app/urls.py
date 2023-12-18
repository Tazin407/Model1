from django.urls import path,include
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('/deletedata/<int:roll>', views.deletedata, name='deletedata'),
]