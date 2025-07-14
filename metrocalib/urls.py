from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('index2/', views.index2, name='index2'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('dashboard', views.dashboard, name='dashboard'),
]
