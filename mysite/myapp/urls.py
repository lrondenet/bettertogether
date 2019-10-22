from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('login/', auth_views.LoginView.as_view()),
]
