from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', homepage, name='home'),
    path('register/', registerpage, name='register'),
    path("login/", LoginView.as_view(template_name="Main/login.html"), name="login"),  #NOTE LoginView is a class in django and to use it as a page function we must add "as_view"
    path("logout/", LogoutView.as_view(template_name="Main/logout.html"), name="logout"),
    path('register2/', frontend_register, name='register2'),
    path('login2/', frontend_login, name='login2'),
    path('logout2/', frontend_logout, name='logout2')
]