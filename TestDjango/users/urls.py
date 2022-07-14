from django.urls import path, include
from users.views import Register, history_view
from .views import home_view, redirect_url_view
from django.contrib.auth import views

appname = "shortener"

urlpatterns = (
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path('register/', Register.as_view(), name='register'),
    path('', home_view, name='home'),
    path('<str:shortened_part>', redirect_url_view, name='redirect'),
    path('history/', history_view, name="history")
)