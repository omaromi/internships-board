from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='board-home'),
    path('add_internship/',views.add_internship,name='add-internship'),
    path('show_internship/<internship_id>/',views.show_internship,name='show-internship'),
    path('staff/',views.staffmembers,name='board-staff'),
    path('add_company/', views.add_company, name='add-company'),
    path('staff_internships/<staff_id>',views.staff_internships,name='staff-internships'),
    path('update_internship/<internship_id>',views.update_internship,name='update-internship'),
    path('staff_login',views.staff_login,name='staff-login'),
]