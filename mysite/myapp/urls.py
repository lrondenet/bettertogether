from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('login/', auth_views.LoginView.as_view()),
]
