from django.urls import path
from website import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('user_dashboard', views.user_dashboard, name="user_dashboard"),
    path('update_user', views.update_user, name="update_user"),
]