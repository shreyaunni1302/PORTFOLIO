from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('education/', views.education, name='education'),
    path('project/', views.project, name='project'),
    path('certificate/', views.certificate, name='certificate'),
    path('contact/', views.contact, name='contact'),
]