from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('skateparks/', views.skateparks, name='skateparks'),
]
