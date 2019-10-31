from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url
#from views import user_list
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', views.logout_view),
]
