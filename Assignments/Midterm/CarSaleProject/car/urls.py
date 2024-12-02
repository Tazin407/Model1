from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.show_cars, name='home'),
    path('details/<int:id>', views.CarDetail.as_view(), name='detail'),
]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
