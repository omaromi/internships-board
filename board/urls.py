from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='board-home'),
    # path('intupload/',views.upload,name='board-upload'),
    path('internshipform/',views.add_internship,name='add-internship'),
    path('show_internship/<internship_id>/',views.show_internship,name='show-internship'),
]