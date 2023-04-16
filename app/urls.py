from django.urls import path, include
from app import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('register/', views.Register.as_view()),
    path('contact/', views.Contact.as_view()),
    path('contact/<int:pk>/', views.ContactRetrieveUpdateDestroyView.as_view()),
]
