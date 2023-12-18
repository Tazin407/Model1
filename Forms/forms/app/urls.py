from django.urls import path,include
from.import views

urlpatterns = [
    path('', views.form, name='form' ),
    path('account/', views.account, name='account'),
    path('djangoForm/', views.djangoForm, name='djangoForm'),
    path('studentForm/', views.StudentData, name='studentForm'),
]