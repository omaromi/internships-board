from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='board-home'),
    path('intupload/',views.upload,name='board-upload')
]